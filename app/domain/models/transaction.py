from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.domain.models.base_model import BaseModel
from core.db import db

class Transaction(db.Model, BaseModel):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, index=True)
    total_value = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    clientName = Column(String(100), nullable=False)
    clientCPF = Column(String(11), nullable=True)
