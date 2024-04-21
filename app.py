from flask import Flask, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel

app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="162981605834", location="us-central1")
model = GenerativeModel("projects/162981605834/locations/us-central1/endpoints/1269212451430203392")

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.json.get('symptoms')
    responses = model.generate_content(
        [f"given a patient reporting: {user_input}\ngenerate a single relevant diagnostic question to further assess their condition:"],
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 1,
            "top_p": 1,
        },
        safety_settings={
            "HARM_CATEGORY_HATE_SPEECH": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
        },
    )
    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
