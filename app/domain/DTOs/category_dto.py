from app.domain.DTOs.base_dto import BaseDTO


class CategoryDTO(BaseDTO):
    def __init__(
        self,
        name: str,
        description: str = "",
        id: int = None,
    ):
        super().__init__(id)
        self.name = name
        self.description = description
