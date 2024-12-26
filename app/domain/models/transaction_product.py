from sqlalchemy import Column, Integer, ForeignKey
from app.domain.models.base_model import BaseModel
from core.db import db

class TransactionProduct(db.Model, BaseModel):
  __tablename__ = "transaction_product"
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  idTransaction = Column(Integer, ForeignKey('transaction.id'), nullable=False)
  idProduct = Column(Integer, ForeignKey('product.id'), nullable=False)
  productAmount = Column(Integer, nullable=False)
  