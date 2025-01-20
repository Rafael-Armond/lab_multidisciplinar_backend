from typing import Dict

from flask import jsonify
from app.domain.DTOs.product_dto import ProductDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.models.product import Product


class ProductMapper(BaseMapper[ProductDTO]):
    @staticmethod
    def productEntityToProductDto(entity: Product) -> ProductDTO:
        return ProductDTO(
            categoryId=entity.category.id if entity.category else None,
            description=entity.description,
            name=entity.name,
            value=entity.value,
            id=entity.id,
        )

    @staticmethod
    def productDtoToProductEntityMapper(dto: ProductDTO) -> Product:
        return Product(
            name=dto.name,
            value=dto.value,
            description=dto.description,
            categoryId=dto.categoryId,
        )

    @classmethod
    def convertFromDtoToJson(self, dto: ProductDTO) -> dict:
        return {
            "name": dto.name,
            "value": dto.value,
            "description": dto.description,
            "categoryId": dto.categoryId,
            "id": dto.id,
        }

    @classmethod
    def convertFromJsonToDto(self, json: dict) -> ProductDTO:
        return ProductDTO(
            value=json.get("value"),
            name=json.get("name"),
            description=json.get("description"),
            categoryId=json.get("categoryId"),
        )
