# # app/__init__.py
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# # Criação da instância do SQLAlchemy e Migrate
# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     # Cria a instância Flask
#     app = Flask(__name__)

#     # Configurações do banco de dados (exemplo com PostgreSQL)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:admin123@localhost:5432/flaskdb'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # Inicializa as extensões
#     db.init_app(app)
#     migrate.init_app(app, db)

#     # Importa e registra as rotas de usuários
#     from app.routes.user_routes import router as user_router
#     app.register_blueprint(user_router, url_prefix='/api/v1')

#     return app
