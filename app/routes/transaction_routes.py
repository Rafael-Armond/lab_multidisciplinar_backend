from flask import Blueprint, request

from app.domain.models.transaction import Transaction
from app.repository.implementations.base_repository import BaseRepository
from app.repository.implementations.transaction_repository import TransactionRepository
from app.routes.base_routes import BaseRoutes
from app.useCases.transaction.create_transaction_useCase import CreateTransactionUseCase
from app.useCases.transaction.delete_transaction_useCase import DeleteTransactionUseCase
from app.useCases.transaction.get_all_transactions_useCase import (
    GetAllTransactionsUseCase,
)
from app.useCases.transaction.get_transaction_useCase import GetTransactionUseCase
from app.useCases.transaction.update_transaction_useCase import UpdateTransactionUseCase
from core.db import get_session


class TransactionRoutes(BaseRoutes):
    def __init__(self, blueprint: Blueprint):
        transactionRepository: BaseRepository = TransactionRepository(
            session=get_session(), model=Transaction
        )
        self.router = blueprint
        self.register_routes(controllerName="/transactions")
        self.createTransactionUseCase = CreateTransactionUseCase(
            respository=transactionRepository
        )
        self.getAllTransactionsUseCase = GetAllTransactionsUseCase(
            respository=transactionRepository
        )
        self.getTransactionByIdUseCase = GetTransactionUseCase(
            respository=transactionRepository
        )
        self.deleteTransactionUseCase = DeleteTransactionUseCase(
            respository=transactionRepository
        )
        self.updateTransactionUseCase = UpdateTransactionUseCase(
            respository=transactionRepository
        )

    def register_routes(self, controllerName: str):
        self.router.add_url_rule(
            controllerName, view_func=self.create_transaction, methods=["POST"]
        )
        self.router.add_url_rule(
            controllerName, view_func=self.get_all_transactions, methods=["GET"]
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>",
            view_func=self.get_transaction,
            methods=["GET"],
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>",
            view_func=self.delete_transaction,
            methods=["DELETE"],
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>",
            view_func=self.update_transaction,
            methods=["PUT"],
        )

    def create_transaction(self):
        return self.createTransactionUseCase.execute(transactionData=request.get_json())

    def get_transaction(self, id):
        return self.getTransactionByIdUseCase.execute(transactionId=id)

    def get_all_transactions(self):
        return self.getAllTransactionsUseCase.execute()

    def update_transaction(self, id):
        return self.updateTransactionUseCase.execute(
            transactionId=id, transactionData=request.get_json()
        )

    def delete_transaction(self, id):
        return self.deleteTransactionUseCase.execute(transactionId=id)


transaction_routes = TransactionRoutes(Blueprint("transaction_routes", __name__))
