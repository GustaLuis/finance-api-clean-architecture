
from domain.repositories.account_repository import AccountRepository
from application.dtos.transaction_dto import AccountOutput
from uuid import UUID

class ListAccountsUseCase:
    def __init__(self, account_repository: AccountRepository):
        self._account_repository = account_repository

    async def execute(self, account_id: UUID) -> list[AccountOutput]:
        accounts = await self._account_repository.list_by_user(account_id)

        return [
            AccountOutput(
                account_id=account.id,
                user_id=account.user_id,
                name=account.name,
                balance=account.balance
            ) 
            for account in accounts
        ]