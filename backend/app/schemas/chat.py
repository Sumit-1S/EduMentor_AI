from pydantic import BaseModel
from datetime import datetime

class ChatSessionCreate(BaseModel):
    title:str

class ChatSessionResponse(BaseModel):
    id: int
    title: str
    created_at:datetime

    model_config={
        "from_attribute": True
    }

class ChatRequest(BaseModel):
    session_id: int
    prompt: str