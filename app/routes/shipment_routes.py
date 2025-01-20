from flask import Blueprint, request
from app.routes.base_routes import BaseRoutes
from app.useCases.shipment.create_shipment_use_case import CreateShipmentUseCase


class ShipmentRoutes(BaseRoutes):
    def __init__(self, blueprint: Blueprint):
        self.router = blueprint
        self.register_routes(controllerName="/shipments")
        self.createShipmentUseCase = CreateShipmentUseCase()

    def register_routes(self, controllerName: str) -> None:
        self.router.add_url_rule(
            controllerName, view_func=self.create_shipment, methods=["POST"]
        )

    def create_shipment(self):
        return self.createShipmentUseCase.execute(data=request.get_json())


shipment_routes = ShipmentRoutes(Blueprint("shipment_routes", __name__))
