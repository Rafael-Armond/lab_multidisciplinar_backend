from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import db

class Product(db.Model):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    value = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    categoryId = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", back_populates="products")
    transactions = relationship("Transaction", back_populates="product")
