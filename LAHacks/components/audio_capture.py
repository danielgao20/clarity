from urllib.request import urlopen

import os
import reflex as rx

from reflex_audio_capture import AudioRecorderPolyfill, get_codec, strip_codec_part

from openai import AsyncOpenAI

api_key = os.getenv('OPENAI_API_KEY')

client = AsyncOpenAI(api_key=api_key)

REF = "myaudio"


class State(rx.State):
    """The app state."""

    has_error: bool = False
    processing: bool = False
    transcript: list[str] = []
    timeslice: int = 0
    device_id: str = ""
    use_mp3: bool = True

    latest_transcript: str = "No transcript available."
    def update_latest_transcript(self):
        if self.transcript:
            self.latest_transcript = self.transcript[-1]
        else:
            self.latest_transcript = "No transcript available."

    async def on_data_available(self, chunk: str):
        mime_type, _, codec = get_codec(chunk).partition(";")
        audio_type = mime_type.partition("/")[2]
        if audio_type == "mpeg":
            audio_type = "mp3"
        print(len(chunk), mime_type, codec, audio_type)
        with urlopen(strip_codec_part(chunk)) as audio_data:
            try:
                self.processing = True
                yield
                transcription = await client.audio.transcriptions.create(
                    model="whisper-1",
                    file=("temp." + audio_type, audio_data.read(), mime_type),
                )
                self.transcript.append(transcription.text)
                self.update_latest_transcript()
            except Exception as e:
                self.has_error = True
                yield capture.stop()
                raise
            finally:
                self.processing = False
            self.transcript.append(transcription.text)

    def set_timeslice(self, value):
        self.timeslice = value[0]

    def set_device_id(self, value):
        self.device_id = value
        yield capture.stop()

    def on_error(self, err):
        print(err)

    def on_load(self):
        # We can start the recording immediately when the page loads
        return capture.start()


capture = AudioRecorderPolyfill.create(
    id=REF,
    on_data_available=State.on_data_available,
    on_error=State.on_error,
    timeslice=State.timeslice,
    device_id=State.device_id,
    use_mp3=State.use_mp3,
)

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            capture,
            rx.text(f"Recorder Status: {capture.recorder_state}", font_family="Metropolis", align="center",),
            rx.cond(
                capture.is_recording,
                rx.button(
                    "Stop Recording", 
                    on_click=capture.stop(),
                    size="3",
                    font_family="Metropolis",
                    background_color="#1B3EF3",
                ),
                rx.button(
                    "Start Recording",
                    on_click=capture.start(),
                    size="3",
                    font_family="Metropolis",
                    background_color="#1B3EF3",
                ),
            ),
            rx.card(
                rx.text("Transcript"),
                rx.divider(),
                rx.text(State.latest_transcript),
                rx.cond(
                    State.processing,
                    rx.text("..."),
                ),
            ),
            style={"width": "100%", "> *": {"width": "100%"}},
        ),
        size="1",
        margin_y="2em",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
