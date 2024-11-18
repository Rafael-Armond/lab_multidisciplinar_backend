from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
 

db = SQLAlchemy()
migrate = Migrate()

engine = create_engine("postgresql+psycopg2://admin:admin123@localhost:5432/flaskdb", echo=True)

# Sessão e Base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session():
  return Session(bind=engine)