from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.domain.models.base_model import BaseModel
from core.db import db


class Product(db.Model, BaseModel):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    value = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    categoryId = Column(Integer, ForeignKey("category.id"), nullable=False)

    category = db.relationship("Category", lazy="joined")
