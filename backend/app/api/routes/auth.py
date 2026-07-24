from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import  UserCreate, UserResponse, UserLogin
from app.services.auth_services import register_user, login_user
from app.core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = register_user(db, user)

    if new_user is None:
        raise HTTPException(
            status_code=400, 
            details="Email already registered."
        )

    return new_user

@router.post("/login")
def login(
    user:UserLogin,
    db: Session=Depends(get_db)
):
    db_user = login_user(
        db, 
        user.email,
        user.password
    )
    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token=create_access_token(
        {
            "sub": db_user.email
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }