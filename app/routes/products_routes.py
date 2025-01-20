from flask import Blueprint, request

from app.domain.models.product import Product
from app.repository.implementations.base_repository import BaseRepository
from app.repository.implementations.product_repository import ProductRepository
from app.routes.base_routes import BaseRoutes
from app.useCases.product.create_product_useCase import CreateProductUseCase
from app.useCases.product.delete_product_useCase import DeleteProductUseCase
from app.useCases.product.get_all_products_useCase import GetAllProductsUseCase
from app.useCases.product.get_product_useCase import GetProductUseCase
from app.useCases.product.update_product_useCase import UpdateProductUseCase
from core.db import get_session


class ProductsRoutes(BaseRoutes):
    def __init__(self, blueprint: Blueprint):
        productRepository: BaseRepository = ProductRepository(
            session=get_session(), model=Product
        )

        self.router = blueprint
        self.register_routes(controllerName="/products")
        self.createProductUseCase = CreateProductUseCase(respository=productRepository)
        self.getAllProductsUseCase = GetAllProductsUseCase(
            respository=productRepository
        )
        self.getProductByIdUseCase = GetProductUseCase(respository=productRepository)
        self.deleteProductUseCase = DeleteProductUseCase(respository=productRepository)
        self.updateProductUseCase = UpdateProductUseCase(respository=productRepository)

    def register_routes(self, controllerName: str) -> None:
        self.router.add_url_rule(
            controllerName, view_func=self.create_product, methods=["POST"]
        )
        self.router.add_url_rule(
            controllerName, view_func=self.get_all_products, methods=["GET"]
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>", view_func=self.get_product, methods=["GET"]
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>",
            view_func=self.delete_product,
            methods=["DELETE"],
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>", view_func=self.update_product, methods=["PUT"]
        )

    def create_product(self):
        return self.createProductUseCase.execute(productData=request.get_json())

    def get_product(self, id):
        return self.getProductByIdUseCase.execute(productId=id)

    def get_all_products(self):
        return self.getAllProductsUseCase.execute()

    def update_product(self, id):
        return self.updateProductUseCase.execute(
            productId=id, productData=request.get_json()
        )

    def delete_product(self, id):
        return self.deleteProductUseCase.execute(productId=id)


product_routes = ProductsRoutes(Blueprint("product_routes", __name__))
