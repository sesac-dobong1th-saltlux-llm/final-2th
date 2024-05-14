# schemas.py (이 정보를 토대로 FastAPI request 보냄)
from pydantic import BaseModel
from datetime import datetime
from typing import Union


# class ResponseMemo(BaseModel):
#    id: int
#    title: str
#    content: Union[str, None] = None
#    is_favorite: bool = False

#    class Config:
#        orm_mode = True


# 사용자 정보
class UserBase(BaseModel):
    user_id: str
    password: str
    # gender: str
    name: str
    # age: int
    # email: str = None
    # address: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    # id: int
    user_id: str
    password: str
    # gender: str
    name: str
    # age: int
    # email: str = None
    # address: str

    class Config:
        orm_mode = True


# 채팅방
class ChatroomBase(BaseModel):
    chatroom_name: str
    datetime_chatroom: datetime
    user_id: str
    llm_name: str

    class Config:
        orm_mode = True


class ChatroomResponse(BaseModel):
    chatroom_id: int
    chatroom_name: str
    datetime_chatroom: datetime
    user_id: str
    llm_name: str

    class Config:
        orm_mode = True


# 채팅 내 대화문
class DialogueBase(BaseModel):
    chatroom_id: str
    datetime_dialog: datetime
    user_sentence: str
    bot_sentence: str


class DialogueResponse(BaseModel):
    dialog_id: int
    chatroom_id: str
    datetime_dialog: datetime
    user_sentence: str
    bot_sentence: str
