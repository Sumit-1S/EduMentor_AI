from app.database.database import engine
from app.database.database import Base

from app.models.user import User

def create_tables():
    Base.metadata.create_all(bind=engine)