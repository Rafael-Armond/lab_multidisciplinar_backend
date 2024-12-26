from flask import jsonify
from app.domain.DTOs.product_dto import ProductDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.product_mapper import ProductMapper
from app.domain.models.product import Product
from app.repository.implementations.product_repository import ProductRepository


class UpdateProductUseCase:
    def __init__(self, respository: ProductRepository):
        self.product_repository: ProductRepository = respository
        self.product_mapper: BaseMapper = ProductMapper()

    def execute(self, productId: int, productData: dict) -> dict:
        try:
            if not self.product_repository.read(productId):
                raise ValueError(f"Product {productId} not found")

            productDto: ProductDTO = self.product_mapper.convertFromJsonToDto(
                productData
            )
            productEntity: Product = ProductMapper().productDtoToProductEntityMapper(
                productDto
            )
            productEntity.id = productId
            updatedProduct: ProductDTO = ProductMapper().productEntityToProductDto(
                self.product_repository.update(productEntity)
            )

            return (
                jsonify(
                    {
                        "message": "Product updated successfully",
                        "data": self.product_mapper.convertFromDtoToJson(
                            updatedProduct
                        ),
                    }
                ),
                200,
            )

        except ValueError as ve:
            return (
                jsonify({"message": str(ve), "data": None}),
                404,
            )

        except Exception as e:
            return (
                jsonify({"message": f"Erro ao atualizar produto. {e}", "data": None}),
                500,
            )
