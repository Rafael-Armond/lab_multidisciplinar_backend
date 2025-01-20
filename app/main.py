from flask import Flask
from core.db import db, migrate
from app.routes.user_routes import user_routes
from app.routes.products_routes import product_routes
from app.routes.categories_routes import category_routes
from app.routes.shipment_routes import shipment_routes
from app.routes.orders_routes import orders_routes
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Configuração do PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://admin:admin123@localhost:5432/flaskdb"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

url_prefix_v1 = "/api/v1"

app.register_blueprint(user_routes.router, url_prefix=url_prefix_v1)
app.register_blueprint(product_routes.router, url_prefix=url_prefix_v1)
app.register_blueprint(category_routes.router, url_prefix=url_prefix_v1)
app.register_blueprint(shipment_routes.router, url_prefix=url_prefix_v1)
app.register_blueprint(orders_routes.router, url_prefix=url_prefix_v1)

if __name__ == "__main__":
    app.run(debug=True)

"""
TODO: 
Link para um tutorial que usa Flask com kafka streams. 
- https://subham-sahoo.medium.com/live-data-streaming-project-using-kafka-part-1-9e7553c70b1

Vídeo sobre o mesmo tópico: 
- https://www.youtube.com/watch?v=hfi_ALPlsOQ
"""
