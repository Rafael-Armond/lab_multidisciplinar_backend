from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from db import db

class TesteTable(db.Model):
    __tablename__ = "teste"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    transactions = relationship("Transaction", back_populates="teste")
