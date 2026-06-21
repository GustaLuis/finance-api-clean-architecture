from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class Account:
    id: UUID
    user_id: UUID
    name: str
    balance: Decimal

    def withdraw(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if amount > self.balance:
            from domain.exceptions import InsufficientFundsError
            raise InsufficientFundsError(
                f"Saldo insuficiente: disponível {self.balance}, solicitado {amount}"
            )
        self.balance -= amount

    def deposit(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.balance += amount
