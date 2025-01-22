from flask_socketio import SocketIO, emit
from flask import Flask, request
from core.db import db, migrate
from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins="*")  # Criando o socketio fora da função


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Configuração do PostgreSQL
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql+psycopg2://admin:admin123@localhost:5432/flaskdb"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Importação das rotas dentro da função para evitar importação circular
    from app.routes.orders_routes import orders_routes
    from app.routes.user_routes import user_routes
    from app.routes.products_routes import product_routes
    from app.routes.categories_routes import category_routes
    from app.routes.shipment_routes import shipment_routes

    url_prefix_v1 = "/api/v1"

    app.register_blueprint(user_routes.router, url_prefix=url_prefix_v1)
    app.register_blueprint(product_routes.router, url_prefix=url_prefix_v1)
    app.register_blueprint(category_routes.router, url_prefix=url_prefix_v1)
    app.register_blueprint(shipment_routes.router, url_prefix=url_prefix_v1)
    app.register_blueprint(orders_routes.router, url_prefix=url_prefix_v1)

    socketio.init_app(app)  # Inicializando o SocketIO após a criação do app

    return app


# WebSocket para clientes ouvirem novos pedidos
@socketio.on("connect")
def handle_connect():
    print("Cliente conectado:", request.sid)
    emit("server_message", {"message": "Bem-vindo ao sistema de pedidos!"})


@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado:", request.sid)


if __name__ == "__main__":
    app = create_app()
    socketio.run(app, debug=True, host="0.0.0.0", port=5000, use_reloader=False)
