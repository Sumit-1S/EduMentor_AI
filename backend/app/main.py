from fastapi import FastAPI
from app.core.config import settings

from app.database.database import engine
from app.database.database import Base

Base.metadata.create_all(bind=engine)

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