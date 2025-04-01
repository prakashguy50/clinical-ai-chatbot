![alt text](image-1.png)

clinical-chatbot/
├── app/
│ ├── main.py # FastAPI app
│ ├── vertex_ai_service.py # Vertex AI integration
│ └── models/ # (optional)
│ └── schema.py
├── requirements.txt
├── Dockerfile
├── frontend/ # React UI
│ └── src/
│ └── components/
│ └── ChatInterface.jsx
└── README.md

![alt text](image.png)
Note: Ensure Vertex AI API is enabled in your Google Cloud project

Frontend Setup
![alt text](image-2.png)
Note: Backend must be running at localhost:8080

☁️ Deployment
Backend (Cloud Run)
![alt text](image-3.png)

Frontend (Vercel)
Push frontend code to a GitHub repository

Create new project in Vercel

Import GitHub repository

Set environment variable REACT_APP_API_URL to your Cloud Run endpoint

Deploy

❓ Example Queries
What are the symptoms of diabetes?

How is hypertension treated in elderly patients?

What is the recommended dosage of metformin?

💬 License
MIT License - see LICENSE for details

Important: Replace all environment variables (your-project-id) with your actual GCP credentials before deployment.