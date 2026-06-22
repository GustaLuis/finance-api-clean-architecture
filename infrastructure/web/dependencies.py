from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from application.use_cases.create_transaction import CreateTransactionUseCase
from infrastructure.database.repositories.sqlalchemy_account_repository import (
    SQLAlchemyAccountRepository,
)
from infrastructure.database.repositories.sqlalchemy_transaction_repository import (
    SQLAlchemyTransactionRepository,
)
from infrastructure.database.session import get_session

from application.use_cases.create_account import CreateAccountUseCase
from application.use_cases.get_account import GetAccountUseCase
from application.use_cases.list_accounts import ListAccountsUseCase

def get_account_repository(session: AsyncSession = Depends(get_session)):
    return SQLAlchemyAccountRepository(session)


def get_transaction_repository(session: AsyncSession = Depends(get_session)):
    return SQLAlchemyTransactionRepository(session)


def get_create_transaction_use_case(
    account_repo: SQLAlchemyAccountRepository = Depends(get_account_repository),
    transaction_repo: SQLAlchemyTransactionRepository = Depends(get_transaction_repository),
) -> CreateTransactionUseCase:
    return CreateTransactionUseCase(
        account_repository=account_repo,
        transaction_repository=transaction_repo,
    )

def get_create_account_use_case(
    account_repo: SQLAlchemyAccountRepository = Depends(get_account_repository),
) -> CreateAccountUseCase:
    return CreateAccountUseCase(account_repository=account_repo)

def get_get_account_use_case(
    account_repo: SQLAlchemyAccountRepository = Depends(get_account_repository),
) -> GetAccountUseCase:
    return GetAccountUseCase(account_repository=account_repo)


def get_list_accounts_use_case(
    account_repo: SQLAlchemyAccountRepository = Depends(get_account_repository),
) -> ListAccountsUseCase:
    return ListAccountsUseCase(account_repository=account_repo)
