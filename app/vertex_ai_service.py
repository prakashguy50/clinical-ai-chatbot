import vertexai
from vertexai.generative_models import GenerativeModel
import os

PROJECT_ID = os.getenv("GCP_PROJECT_ID", "genai-455516")
REGION = os.getenv("GCP_REGION", "us-central1")

vertexai.init(project=PROJECT_ID, location=REGION)
model = GenerativeModel.from_pretrained("gemini-2.0-flash")

def get_vertexai_response(prompt: str) -> str:
    response = model.predict(
        prompt,
        temperature=0.7,
        max_output_tokens=512,
        top_k=40,
        top_p=0.8,
    )
    return response.text
