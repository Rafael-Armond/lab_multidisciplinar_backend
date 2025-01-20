from app.domain.DTOs.product_dto import ProductDTO


class PurchasedProductDTO(ProductDTO):
    def __init__(self, product_dto: ProductDTO, amount: int):
        super().__init__(
            name=product_dto.name,
            value=product_dto.value,
            categoryId=product_dto.categoryId,
            description=product_dto.description,
            id=product_dto.id,
        )
        self.amount = amount
