from flask import jsonify
from app.domain.DTOs.transaction_dto import TransactionDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.models.transaction import Transaction


class TransactionMapper(BaseMapper[TransactionDTO]):
    @staticmethod
    def transactionEntityToTransactionDto(entity: Transaction) -> TransactionDTO:
        return TransactionDTO(
            client_cpf=entity.clientCPF,
            client_name=entity.clientName,
            created_at=entity.created_at,
            total_value=entity.total_value,
        )

    @staticmethod
    def transactionDtoToTransactionEntityMapper(dto: TransactionDTO) -> Transaction:
        return Transaction(
            clientCPF=dto.clientCPF,
            clientName=dto.clientName,
            created_at=dto.created_at,
            total_value=dto.total_value,
        )

    @classmethod
    def convertFromDtoToJson(self, dto: TransactionDTO) -> dict:
        return jsonify(
            {
                "total_value": dto.total_value,
                "created_at": dto.created_at,
                "clientName": dto.clientName,
                "clientCPF": dto.clientCPF,
                "purchased_products": dto.purchased_products,
            }
        )

    @classmethod
    def convertFromJsonToDto(self, json: dict) -> TransactionDTO:
        return TransactionDTO(
            total_value=json.get("total_value"),
            created_at=json.get("created_at"),
            clientName=json.get("clientName"),
            clientCPF=json.get("clientCPF"),
            purchased_products=json.get("purchased_products", []),
        )
