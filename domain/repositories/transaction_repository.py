from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    async def save(self, transaction: Transaction) -> None:
        ...

    @abstractmethod
    async def list_by_account(self, account_id: UUID) -> list[Transaction]:
        ...
