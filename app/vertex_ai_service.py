import vertexai
from vertexai.language_models import TextGenerationModel
import os

PROJECT_ID = os.getenv("GCP_PROJECT_ID", "healthvision-ml-dev")
REGION = os.getenv("GCP_REGION", "us-central1")

vertexai.init(project="healthvision-ml-dev", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison")

def get_vertexai_response(prompt: str) -> str:
    response = model.predict(
        prompt,
        temperature=0.7,
        max_output_tokens=512,
        top_k=40,
        top_p=0.8,
    )
    return response.text
