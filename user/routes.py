from fastapi import APIRouter, Depends
from .schemas import User
from .models import User as UserModel
from sqlalchemy.orm import Session
from auth.dependencies import get_current_user, get_db

router = APIRouter()

@router.get("/me", response_model=User)
def read_users_me(current_user: Session = Depends(get_current_user) ):
    return current_user