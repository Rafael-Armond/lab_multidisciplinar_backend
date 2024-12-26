from flask import jsonify
from app.domain.DTOs.product_dto import ProductDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.product_mapper import ProductMapper
from app.domain.models.product import Product
from app.repository.implementations.product_repository import ProductRepository


class GetProductUseCase:
    def __init__(self, respository: ProductRepository):
        self.product_repository: ProductRepository = respository
        self.product_mapper: ProductMapper = ProductMapper()

    def execute(self, productId: int) -> dict:
        productEntity: Product = self.product_repository.read(entity_id=productId)
        productDto: ProductDTO = ProductMapper.productEntityToProductDto(
            entity=productEntity
        )

        if productEntity:
            return (
                jsonify(
                    {
                        "message": "Produto encontrado.",
                        "data": self.product_mapper.convertFromDtoToJson(productDto),
                    }
                ),
                200,
            )
        else:
            raise ValueError(f"Product {productId} not found.")
