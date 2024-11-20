from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.domain.models.base_model import BaseModel
from core.db import db

class Category(db.Model, BaseModel):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    products = relationship("Product", back_populates="category")
