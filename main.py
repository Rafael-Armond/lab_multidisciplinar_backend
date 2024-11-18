from flask import Flask
from db import db, migrate
from models import *
from repository import Respository
from db import get_session

app = Flask(__name__)

# Configuração do MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://admin:admin123@localhost:5432/flaskdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa o banco de dados e migrações
db.init_app(app)
migrate.init_app(app, db)

@app.route("/create-user")
def hello_world():
    repository = Respository(session=get_session())
    repository.insert_user(username="Rafael Maia", role="admin123", created_at="2024-11-18")
    return "Usuário cadastrado."

if __name__ == "__main__":
    app.run(debug=True)
