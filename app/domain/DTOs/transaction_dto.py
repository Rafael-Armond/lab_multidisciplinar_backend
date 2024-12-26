from datetime import datetime


class TransactionDTO:
    def __init__(
        self,
        total_value: float,
        created_at: datetime,
        client_name: str,
        client_cpf: str,
        purchased_products: list[int],
    ):
        super().__init__(id)
        self.total_value = total_value
        self.created_at = created_at
        self.clientName = client_name
        self.clientCPF = client_cpf
        self.purchased_products = purchased_products
