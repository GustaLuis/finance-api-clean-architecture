from uuid import UUID

from application.dtos.transaction_dto import AccountOutput
from domain.repositories.account_repository import AccountRepository
from domain.exceptions import AccountNotFoundError


class GetAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self._account_repository = account_repository

    async def execute(self, account_id: UUID) -> AccountOutput:
        account = await self._account_repository.get_by_id(account_id)
        if account is None:
            raise AccountNotFoundError(f"Conta {account_id} não encontrada")
        
        return AccountOutput(
            account_id=account.id,
            user_id=account.user_id,
            name=account.name,
            balance=account.balance
        )