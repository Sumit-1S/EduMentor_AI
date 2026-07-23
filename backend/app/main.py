from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="EduMentor AI",
    description="AI Learning Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to EduMentor AI!!!",
        "database": settings.DATABASE_URL
    }

@app.get("/health")
def health():
    return {
        "message": "Healthy"
    }