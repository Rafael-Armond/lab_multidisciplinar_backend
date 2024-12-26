from flask import jsonify
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.product_mapper import ProductMapper
from app.repository.implementations.product_repository import ProductRepository


class GetAllProductsUseCase:
    def __init__(self, respository: ProductRepository):
        self.product_repository: ProductRepository = respository
        self.product_mapper: BaseMapper = ProductMapper()

    def execute(self):
        products = self.product_repository.read_all()
        productsDto = [
            ProductMapper().productEntityToProductDto(product) for product in products
        ]

        return (
            jsonify(
                {
                    "message": "Produtos obtidos com sucesso!",
                    "data": [
                        ProductMapper().convertFromDtoToJson(product)
                        for product in productsDto
                    ],
                }
            ),
            200,
        )
