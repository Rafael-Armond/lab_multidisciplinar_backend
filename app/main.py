from flask import Flask
from core.db import db, migrate
from app.routes.user_routes import user_routes  

app = Flask(__name__)

# Configuração do PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://admin:admin123@localhost:5432/flaskdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_routes.router, url_prefix='/api/v1')

if __name__ == "__main__":
    app.run(debug=True)
