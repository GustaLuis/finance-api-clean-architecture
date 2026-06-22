from uuid import uuid4

from application.dtos.account_dto import CreateAccountInput, CreateAccountOutput
from domain.entities.account import Account
from domain.repositories.account_repository import AccountRepository


class CreateAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self._account_repo = account_repository

    async def execute(self, input_data: CreateAccountInput) -> CreateAccountOutput:
        account = Account(
            id=uuid4(),
            user_id=input_data.user_id,
            name=input_data.name,
            balance=input_data.initial_balance,
        )

        await self._account_repo.save(account)

        return CreateAccountOutput(
            account_id=account.id,
            name=account.name,
            balance=account.balance,
        )