from app.domain.models.base_model import BaseModel
from app.domain.models.product import Product


class Shipment(BaseModel):
    def __init__(self, product: Product, amount):
        self.product: Product = product
        self.amount = amount
