from fastapi import FastAPI
from app.core.config import settings

from app.database.database import engine
from app.database.database import Base

from app.database.init_db import create_tables
from app.api.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI(
    title="EduMentor AI",
    description="AI Learning Platform",
    version="1.0.0"
)

app.include_router(auth_router)

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


