from flask import jsonify
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.product_mapper import ProductMapper
from app.repository.implementations.product_repository import ProductRepository


class DeleteProductUseCase:
    def __init__(self, respository: ProductRepository):
        self.product_repository: ProductRepository = respository
        self.product_mapper: BaseMapper = ProductMapper()

    def execute(self, productId: int):
        try:
            self.product_repository.delete(productId)
            return jsonify({"message": "Produto deletado com sucesso.", "data": True})
        except Exception as e:
            raise Exception(f"Error deleting product: {e}")
