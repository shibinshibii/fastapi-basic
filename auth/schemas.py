from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    email: str