from app.domain.DTOs.base_dto import BaseDTO


class ProductDTO(BaseDTO):
    def __init__(
        self,
        name: str,
        value: float,
        categoryId: int,
        description: str = "",
        id: int = None,
    ):
        super().__init__(id)
        self.name = name
        self.value = value
        self.description = description
        self.categoryId = categoryId
