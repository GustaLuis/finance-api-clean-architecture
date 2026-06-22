from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domain.entities.account import Account


class AccountRepository(ABC):
    @abstractmethod
    async def get_by_id(self, account_id: UUID) -> Optional[Account]:
        ...

    @abstractmethod
    async def save(self, account: Account) -> None:
        ...

    @abstractmethod
    async def list_by_user(self, user_id: UUID) -> list[Account]:
        ...
