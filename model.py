from sqlalchemy import Column, Integer, String, Text,  ForeignKey, Boolean, Float, DateTime, Date
from sqlalchemy.orm import relationship
from database import Base


class Config(Base):
    __tablename__ = "config"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, primary_key=True, index=True)


class Chatbot(Base):
    __tablename__ = "chatbot"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=True)
    answer = Column(Text, nullable=True)
    config_id = Column(Integer, ForeignKey("config.id"))