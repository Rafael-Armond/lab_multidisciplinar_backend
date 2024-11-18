from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import db

class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    products = relationship("Product", back_populates="category")
