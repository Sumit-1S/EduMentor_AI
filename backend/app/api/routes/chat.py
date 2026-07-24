from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.chat import ChatSessionCreate, ChatSessionResponse
from app.services.chat_services import ChatService
from app.api.dependencies import get_current_user
from app.services.ai_service import AIService
from app.models.user import User
from app.services.chat_services import save_message
from app.llm.gemini import ask_gemini
from app.models.message import ChatMessage
from app.models.chat import ChatSession

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
def chat(prompt: str):
    response = AIService.chat(prompt=prompt)
    return {
        "response": response
    }


@router.post(
    "/session",
    response_model=ChatSessionResponse
)
def create_session(
    data: ChatSessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ChatService.create_session(
        db=db,
        title=data.title,
        user_id = current_user.id
    )

@router.post("/")
def chat(
    session_id: int,
    prompt: str,
    db: Session = Depends(get_db)
):
    session = db.query(ChatSession).filter(
        ChatSession.id==session_id
    ).first()

    save_message(
        db=db,
        session_id=session_id,
        role="user",
        content=prompt
    )
    answer = ask_gemini(prompt=prompt)

    save_message(
        db=db,
        session_id=session.id,
        role="assistant",
        content=answer
    )
    return {
        "response": answer
    }