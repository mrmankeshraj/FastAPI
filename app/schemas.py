from pydantic import BaseModel, EmailStr, ConfigDict, Field, conint
from datetime import datetime


class PostBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    content: str
    published: bool = Field(default=True)


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr 
    created_at: datetime

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    Post: PostResponse
    votes: int



class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    password: str



class UserLogin(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    password: str

class Token(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    access_token: str
    token_type: str 

class TokenData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str = Field(default=None)


class Vote(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    post_id: int
    dir: conint(ge=0, le=1) # type: ignore
