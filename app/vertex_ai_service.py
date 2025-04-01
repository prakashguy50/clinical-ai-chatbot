import vertexai
from vertexai.language_models import TextGenerationModel
import os

PROJECT_ID = "genai-455516"
REGION = "us-central1"

vertexai.init(project=PROJECT_ID, location=REGION)
model = TextGenerationModel.from_pretrained("text-bison@002")

def get_vertexai_response(prompt: str) -> str:
    response = model.predict(
        prompt,
        temperature=0.7,
        max_output_tokens=512,
        top_k=40,
        top_p=0.8,
    )
    return response.text
