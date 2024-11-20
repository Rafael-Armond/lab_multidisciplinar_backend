from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.domain.models.base_model import BaseModel
from core.db import db

class Transaction(db.Model, BaseModel):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, index=True)
    idUser = Column(Integer, ForeignKey("user.id"))
    idProduct = Column(Integer, ForeignKey("product.id"))
    amount = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    clientName = Column(String(100), nullable=False)
    clientCPF = Column(String(11), nullable=False)

    user = relationship("User", back_populates="transactions")
    product = relationship("Product", back_populates="transactions")
