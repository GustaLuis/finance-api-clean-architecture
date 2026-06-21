from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.transaction import Transaction
from domain.repositories.transaction_repository import TransactionRepository
from infrastructure.database.models import TransactionModel


class SQLAlchemyTransactionRepository(TransactionRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, transaction: Transaction) -> None:
        model = TransactionModel(
            id=str(transaction.id),
            account_id=str(transaction.account_id),
            amount=transaction.amount,
            type=transaction.type,
            category=transaction.category,
            description=transaction.description,
            created_at=transaction.created_at,
        )
        self._session.add(model)
        await self._session.commit()

    async def list_by_account(self, account_id: UUID) -> list[Transaction]:
        result = await self._session.execute(
            select(TransactionModel).where(TransactionModel.account_id == str(account_id))
        )
        models = result.scalars().all()
        return [
            Transaction(
                id=UUID(m.id),
                account_id=UUID(m.account_id),
                amount=m.amount,
                type=m.type,
                category=m.category,
                description=m.description,
                created_at=m.created_at,
            )
            for m in models
        ]
