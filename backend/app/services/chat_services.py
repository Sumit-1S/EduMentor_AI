from sqlalchemy.orm import Session

from app.models.chat import ChatSession
from app.models.message import ChatMessage

from app.services.history_service import get_chat_history
from app.AI.llm import ask_llm

class ChatService:
    @staticmethod
    def create_session(
        db: Session,
        title: str,
        user_id: int    
    ):
        session = ChatSession(
            title = title,
            user_id = user_id
        )
        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    @staticmethod
    def chat(
        db: Session, 
        session_id: int,
        prompt: str
    ):
        ChatService.save_message(
            db=db,
            session_id=session_id,
            role="user",
            content=prompt
        )

        history = get_chat_history(
            db=db,
            session_id=session_id
        )

        response = ask_llm(
            history
        )

        ChatService.save_message(
            db=db,
            session_id=session_id,
            role="assistant",
            content=response
        )

        return {
            "response": response
        }

        
    @staticmethod
    def save_message(
        db: Session,
        session_id: int,
        role: str,
        content: str
    ):
        message = ChatMessage(session_id = session_id, role=role, content = content)
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    @staticmethod
    def get_message(
        db: Session,
        session_id: int
    ):
        return (
            db.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.id)
            .all()
        )