from flask import jsonify
from app.domain.DTOs.category_dto import CategoryDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.category_mapper import CategoryMapper
from app.domain.models.category import Category
from app.repository.implementations.base_repository import BaseRepository


class GetAllCategoriesUseCase:
    def __init__(self, repository: BaseRepository):
        self.repository: BaseRepository = repository
        self.category_mapper: BaseMapper = CategoryMapper()

    def execute(self):
        try:
            categoriesEntity: Category = self.repository.read_all()
            categoriesDto: list[CategoryDTO] = [
                CategoryMapper.categoryEntityToCategoryDto(category)
                for category in categoriesEntity
            ]
            categories: dict = [
                self.category_mapper.convertFromDtoToJson(category)
                for category in categoriesDto
            ]

            if categories:
                return jsonify(
                    {
                        "message": "Categorias retornadas com sucesso!",
                        "data": categories,
                        "status": 200,
                    }
                )
            else:
                return jsonify(
                    {
                        "message": "Categorias não encontradas!",
                        "data": None,
                        "status": 500,
                    }
                )
        except:
            raise Exception("Erro ao obter as categorias.")
