from app.database.database import engine
from app.database.database import Base

from app.models.user import User
from app.models.chat import ChatSession
from app.models.message import ChatMessage

def create_tables():
    Base.metadata.create_all(bind=engine)