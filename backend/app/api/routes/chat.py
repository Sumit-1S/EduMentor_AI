from fastapi import APIRouter
from app.llm.gemini import ask_gemini

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
def chat(prompt: str):
    answer = ask_gemini(prompt=prompt)
    return {
        "response": answer
    }
