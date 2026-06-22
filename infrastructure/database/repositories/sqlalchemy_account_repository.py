from decimal import Decimal
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.account import Account
from domain.repositories.account_repository import AccountRepository
from infrastructure.database.models import AccountModel


class SQLAlchemyAccountRepository(AccountRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, account_id: UUID) -> Optional[Account]:
        result = await self._session.execute(
            select(AccountModel).where(AccountModel.id == str(account_id))
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return self._to_entity(model)

    async def save(self, account: Account) -> None:
        result = await self._session.execute(
            select(AccountModel).where(AccountModel.id == str(account.id))
        )
        model = result.scalar_one_or_none()
        if model is None:
            model = AccountModel(id=str(account.id), user_id=str(account.user_id))
            self._session.add(model)

        model.name = account.name
        model.balance = account.balance
        await self._session.commit()
    
    async def list_by_user(self, user_id: UUID) -> list[Account]:
        result = await self._session.execute(
            select(AccountModel).where(AccountModel.user_id == str(user_id))
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    @staticmethod
    def _to_entity(model: AccountModel) -> Account:
        return Account(
            id=UUID(model.id),
            user_id=UUID(model.user_id),
            name=model.name,
            balance=Decimal(model.balance),
        )
