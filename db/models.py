from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    # email = Column(String, unique=True, index=True, nullable=True)  # 이메일 필드가 nullable

    # User와 Chatroom 사이의 1:M 관계 설정
    # chatrooms = relationship("Chatroom", back_populates="user")

class Chatroom(Base):
    __tablename__ = "chatrooms"

    chatroom_id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    chatroom_name = Column(String, nullable=False)
    datetime_chatroom = Column(DateTime(timezone=True), default=func.now())
    user_id = Column(String, nullable=False) # ForeignKey("users.user_id")

    # Chatroom과 User 및 Dialogue 사이의 관계 설정
    # user = relationship("User", back_populates="chatrooms")
    # dialogues = relationship("Dialogue", back_populates="chatroom")

class Dialogue(Base):
    __tablename__ = "dialogues"

    dialogue_id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    chatroom_id = Column(Integer, nullable=False) # ForeignKey("chatrooms.chatroom_id")
    datetime_dialogue = Column(DateTime(timezone=True), default=func.now())
    user_sentence = Column(String, nullable=False)
    bot_sentence = Column(String, nullable=True)

    # Dialogue와 Chatroom 사이의 관계 설정
    # chatroom = relationship("Chatroom", back_populates="dialogues")
