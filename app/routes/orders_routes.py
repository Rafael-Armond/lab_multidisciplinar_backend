from flask import Blueprint, request
from app.routes.base_routes import BaseRoutes
from app.useCases.orders.create_orders_use_case import CreateOrdersUseCase


class OrdersRoutes(BaseRoutes):
    def __init__(self, blueprint: Blueprint):
        self.router = blueprint
        self.register_routes(controllerName="/orders")
        self.createOrdersUseCase = CreateOrdersUseCase()

    def register_routes(self, controllerName: str) -> None:
        self.router.add_url_rule(
            controllerName, view_func=self.create_order, methods=["POST"]
        )

    def create_order(self):
        return self.createOrdersUseCase.execute(data=request.get_json())


orders_routes = OrdersRoutes(Blueprint("orders_routes", __name__))
