from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base

class ChatMessage(Base):
    __tablename__="chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))
    role = Column(Text)
    content = Column(Text)
    created_at = Column(DateTime, default = datetime.utcnow)
    session = relationship("ChatSession", back_populates="messages")