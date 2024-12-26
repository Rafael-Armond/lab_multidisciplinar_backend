from flask import jsonify
from app.domain.DTOs.product_dto import ProductDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.product_mapper import ProductMapper
from app.domain.models.product import Product
from app.repository.implementations.product_repository import ProductRepository


class CreateProductUseCase:
    def __init__(self, respository: ProductRepository):
        self.product_repository: ProductRepository = respository
        self.product_mapper: BaseMapper = ProductMapper()

    def execute(self, productData: dict):
        productDto: ProductDTO = self.product_mapper.convertFromJsonToDto(productData)
        productEntity: Product = ProductMapper().productDtoToProductEntityMapper(
            productDto
        )
        created_product: Product = self.product_repository.create(productEntity)

        if created_product:
            return (
                jsonify(
                    {
                        "message": "Produto criado com sucesso",
                        "data": created_product.id,
                    }
                ),
                201,
            )
        else:
            raise Exception("Error when creating product!")
