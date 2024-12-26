from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app.domain.models.base_model import BaseModel
from core.db import db
from datetime import datetime


class User(BaseModel):
    pass
    # __tablename__ = "user"
    # id = Column(Integer, primary_key=True, index=True)
    # username = Column(String(255), nullable=False)
    # role = Column(String(50), nullable=False)
    # created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    # transactions = relationship("Transaction", back_populates="user")

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "role": self.role,
    #         "created_at": self.created_at,
    #     }
