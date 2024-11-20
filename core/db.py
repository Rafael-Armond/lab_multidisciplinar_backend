from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
 

db = SQLAlchemy()
migrate = Migrate()

engine = create_engine("postgresql+psycopg2://admin:admin123@localhost:5432/flaskdb", echo=True)

def get_session():
  return Session(bind=engine)