from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .dependencies import  get_db, authenticate_user, get_user
from .schemas import UserCreate,UserResponse,TokenSchema
from user.models import User
from .utils import get_password_hash, create_access_token

router = APIRouter()

#login endpoint
@router.post("/token", response_model=TokenSchema)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.email,form_data.password)
    if not user:
        raise  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email and password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub":user.email})

    return {"access token":access_token, "token_type":"bearer"}

#signup endpoint
@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate , db: Session = Depends(get_db)):
    db_user =  get_user(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",

        )
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user