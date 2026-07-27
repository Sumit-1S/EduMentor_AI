from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.chat import ChatSessionCreate, ChatSessionResponse, ChatRequest
from app.services.chat_services import ChatService
from app.api.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

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

@router.post("/send")
def send_message(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    return ChatService.chat(
        db=db,
        session_id=request.session_id,
        prompt=request.prompt
    )