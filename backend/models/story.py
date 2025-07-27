from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import base

class Story(base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    