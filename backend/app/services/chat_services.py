from sqlalchemy.orm import Session
from app.models.chat import ChatSession
from app.models.message import ChatMessage

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