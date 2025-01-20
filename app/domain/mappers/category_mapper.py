from app.domain.DTOs.category_dto import CategoryDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.models.category import Category


class CategoryMapper(BaseMapper[CategoryDTO]):
    @staticmethod
    def categoryEntityToCategoryDto(entity: Category) -> CategoryDTO:
        return CategoryDTO(
            description=entity.description, name=entity.name, id=entity.id
        )

    @classmethod
    def convertFromJsonToDto(self, json: dict):
        return CategoryDTO(
            description=json.get("description"),
            name=json.get("name"),
            id=json.get("id"),
        )

    @classmethod
    def convertFromDtoToJson(self, dto: CategoryDTO) -> dict:
        return {"name": dto.name, "description": dto.description, "id": dto.id}
