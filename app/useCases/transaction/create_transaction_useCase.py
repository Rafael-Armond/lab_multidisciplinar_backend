from flask import jsonify
from app.domain.DTOs.transaction_dto import TransactionDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.transaction_mapper import TransactionMapper
from app.domain.models.transaction import Transaction
from app.domain.models.transaction_product import TransactionProduct
from app.repository.interfaces.ibase_repository import IBaseRepository


class CreateTransactionUseCase:
    def __init__(
        self,
        product_respository: IBaseRepository,
        transaction_product_repository: IBaseRepository,
    ):
        self.transaction_repository: IBaseRepository = product_respository
        self.transaction_product_repository: IBaseRepository = (
            transaction_product_repository
        )
        self.transaction_mapper: BaseMapper = TransactionMapper()

    def __create_transaction_product(self, productDto: TransactionDTO):
        for product in productDto.purchased_products:
            transaction_product: TransactionProduct = TransactionProduct()
            self.transaction_product_repository.create(product)

    def execute(self, transactionData: dict) -> TransactionDTO:
        try:
            transactionDto: TransactionDTO = (
                self.transaction_mapper.convertFromJsonToDto(transactionData)
            )

            # self.__create_transaction_product(
            #     puchased_products=productDto.purchased_products
            # )

            transactionEntity: (
                Transaction
            ) = TransactionMapper().transactionDtoToTransactionEntityMapper(
                transactionDto
            )
            created_transaction: Transaction = self.transaction_repository.create(
                transactionEntity
            )

            print("Id da transação criada: ", created_transaction.id)

            if created_transaction:
                return (
                    jsonify(
                        {
                            "message": "Transação criado com sucesso",
                            "data": created_transaction.id,
                        }
                    ),
                    201,
                )
            else:
                raise Exception("Error when creating product!")
        except Exception as e:
            return (
                jsonify({"message": f"Erro ao criar transação. {e}", "data": None}),
                500,
            )
