from fastapi import FastAPI
from pydantic import BaseModel
from app.vertex_ai_service import get_vertexai_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]  # Replace in production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    answer = get_vertexai_response(query.question)
    return {"answer": answer}
