from flask import jsonify
from app.domain.DTOs.transaction_dto import TransactionDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.transaction_mapper import TransactionMapper
from app.domain.models.transaction import Transaction
from app.repository.interfaces.ibase_repository import IBaseRepository


class CreateTransactionUseCase:
    def __init__(self, respository: IBaseRepository):
        self.transaction_repository: IBaseRepository = respository
        self.transaction_mapper: BaseMapper = TransactionMapper()

    def execute(self, transactionData: dict) -> TransactionDTO:
        productDto: TransactionDTO = self.transaction_mapper.convertFromJsonToDto(
            transactionData
        )
        transactionEntity: Transaction = (
            TransactionMapper().productDtoToProductEntityMapper(productDto)
        )
        created_transaction: Transaction = self.transaction_repository.create(
            transactionEntity
        )

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
