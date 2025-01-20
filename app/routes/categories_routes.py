from flask import Blueprint

from app.domain.models.category import Category
from app.repository.implementations.base_repository import BaseRepository
from app.repository.implementations.category_repository import CategoryRepository
from app.routes.base_routes import BaseRoutes
from app.useCases.category.get_all_categories_use_case import GetAllCategoriesUseCase
from core.db import get_session


class CategoryRoutes(BaseRoutes):
    def __init__(self, blueprint: Blueprint):
        categoryRepository: BaseRepository = CategoryRepository(
            session=get_session(), model=Category
        )

        self.router = blueprint
        self.register_routes(controllerName="/categories")
        self.getAllCategoriesUseCase = GetAllCategoriesUseCase(
            repository=categoryRepository
        )

    def register_routes(self, controllerName: str) -> None:
        self.router.add_url_rule(
            controllerName, view_func=self.get_all_categories, methods=["GET"]
        )

    def get_all_categories(self):
        return self.getAllCategoriesUseCase.execute()


category_routes = CategoryRoutes(Blueprint("category_routes", __name__))
