"""Take screenshots and video recordings from webcam."""
import time
from pathlib import Path
from urllib.request import urlopen
from PIL import Image

import reflex as rx
import reflex_webcam as webcam


# Identifies a particular webcam component in the DOM
WEBCAM_REF = "webcam"
VIDEO_FILE_NAME = "video.webm"

# The path containing the app
APP_PATH = Path(__file__)
APP_MODULE_DIR = APP_PATH.parent
SOURCE_CODE = [
    APP_MODULE_DIR.parent.parent / "LAHacks/components/custom_components/reflex_webcam/webcam.py",
    APP_PATH,
    APP_MODULE_DIR.parent / "requirements.txt",
]

# Mark Upload as used so StaticFiles can get mounted on /_upload
rx.upload()


class VideoState(rx.State):
    last_screenshot: Image.Image | None = None
    last_screenshot_timestamp: str = ""
    loading: bool = False
    recording: bool = False

    def handle_screenshot(self, img_data_uri: str):
        """Webcam screenshot upload handler.
        Args:
            img_data_uri: The data uri of the screenshot (from upload_screenshot).
        """
        if self.loading:
            return
        self.last_screenshot_timestamp = time.strftime("%H:%M:%S")
        with urlopen(img_data_uri) as img:
            self.last_screenshot = Image.open(img)
            self.last_screenshot.load()
            # convert to webp during serialization for smaller size
            self.last_screenshot.format = "WEBP"  # type: ignore

    def _video_path(self) -> Path:
        return Path(rx.get_upload_dir()) / VIDEO_FILE_NAME

    @rx.cached_var
    def video_exists(self) -> bool:
        if not self.recording:
            return self._video_path().exists()
        return False

    def on_start_recording(self):
        self.recording = True
        print("Started recording")
        with self._video_path().open("wb") as f:
            f.write(b"")

    def _strip_codec_part(self, chunk: str) -> str:
        parts = chunk.split(";")
        for part in parts:
            if "codecs=" in part:
                parts.remove(part)
                break
        return ";".join(parts)

    def handle_video_chunk(self, chunk: str):
        print("Got video chunk", len(chunk))
        with self._video_path().open("ab") as f:
            with urlopen(self._strip_codec_part(chunk)) as vid:
                f.write(vid.read())

    def on_stop_recording(self):
        print(f"Stopped recording: {self._video_path()}")
        self.recording = False

    def start_recording(self, ref: str):
        """Start recording a video."""
        return webcam.start_recording(
            ref,
            on_data_available=VideoState.handle_video_chunk,
            on_start=VideoState.on_start_recording,
            on_stop=VideoState.on_stop_recording,
            timeslice=1000,
        )


def last_screenshot_widget() -> rx.Component:
    """Widget for displaying the last screenshot and timestamp."""
    return rx.box(
        rx.cond(
            VideoState.last_screenshot,
            rx.fragment(
                rx.image(src=VideoState.last_screenshot),
                rx.text(VideoState.last_screenshot_timestamp),
            ),
            rx.center(
                rx.text("Click image to capture.", size="4"),
            ),
        ),
    )


def webcam_upload_component(ref: str) -> rx.Component:
    """Component for displaying webcam preview and uploading screenshots.
    Args:
        ref: The ref of the webcam component.
    Returns:
        A reflex component.
    """
    return rx.vstack(
        webcam.webcam(
            id=ref,
            on_click=webcam.upload_screenshot(
                ref=ref,
                handler=VideoState.handle_screenshot,  # type: ignore
            ),
            audio=True,
        ),
        rx.cond(
            VideoState.recording,
            rx.button(
                "Start Recording",
                on_click=VideoState.start_recording(ref),
                background_color="#1B3EF3",
                size="3",
            ),
            rx.button(
                "Stop Recording",
                on_click=webcam.stop_recording(ref),
                background_color="#1B3EF3",
                size="3",
            ),
        ),
        rx.cond(
            VideoState.video_exists,
            rx.link(
                "Download Last Video", href=rx.get_upload_url(VIDEO_FILE_NAME), size="4"
            ),
        ),
        last_screenshot_widget(),
        width="640px",
        align="center",
    )


def index() -> rx.Component:
    return rx.center(
            webcam_upload_component(WEBCAM_REF),
        )


app = rx.App()
app.add_page(index)