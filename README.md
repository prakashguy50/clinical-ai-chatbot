# 🩺 Clinical AI Chatbot – Vertex AI + FastAPI + React

<div align="center">
  <img src="https://img.shields.io/badge/vertex_ai-FF6F00?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Vertex AI">
  <img src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/react-20232a?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React">
</div>

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Deployment](#deployment)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features
- Clinical Q&A with Vertex AI PaLM 2 model
- Real-time chat interface with message history
- Safety filters for medical content validation
- Cloud deployment on GCP Cloud Run + Vercel
- API documentation (Swagger UI) at `/docs`

---

## Architecture

    A[User] --> B[React Frontend]
    B --> C{FastAPI Server}
    C --> D[Vertex AI LLM]
    D --> E[Safety Filters]
    E --> C
    C --> B
    B --> A

Installation
Prerequisites
Google Cloud Project with Vertex AI enabled

Node.js v16+ & Python 3.9+

GCloud CLI installed

Local Development Setup
Clone Repository

git clone git@github.com:prakashguy50/clinical-ai-chatbot.git
cd clinical-ai-chatbot

Backend Setup

pip install -r requirements.txt
export GCP_PROJECT_ID="your-project-id"
export GCP_REGION="us-central1"
gcloud auth application-default login
uvicorn app.main:app --reload --port 8080

Frontend Setup

Deployment
Backend (Google Cloud Run)

gcloud builds submit --tag gcr.io/${GCP_PROJECT_ID}/clinical-chatbot
gcloud run deploy clinical-chatbot \
  --image gcr.io/${GCP_PROJECT_ID}/clinical-chatbot \
  --platform managed \
  --region ${GCP_REGION} \
  --allow-unauthenticated \
  --set-env-vars GCP_PROJECT_ID=${GCP_PROJECT_ID}

Frontend (Vercel)
Set environment variable:

REACT_APP_API_URL="https://your-cloud-run-url.a.run.app"

Deploy:

cd frontend
vercel deploy --prod

Configuration
Environment Variable	Description	Default
GCP_PROJECT_ID	Google Cloud Project ID	Required
GCP_REGION	GCP Region	us-central1
MAX_TOKENS	AI response length	1024
TEMPERATURE	Creativity control (0-1)	0.2
Troubleshooting
Authentication Issues

gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com

CORS Errors
Add to app/main.py:

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Model Not Responding
Verify Vertex AI API is enabled

Check project quotas

Test model directly:

from vertexai.language_models import TextGenerationModel
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict("What is 1+1?")
print(response.text)

License
MIT License - See LICENSE for details

Note
This application demonstrates AI capabilities and should not be used for actual medical diagnosis.
