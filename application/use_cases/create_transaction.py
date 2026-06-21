from application.dtos.transaction_dto import CreateTransactionInput, CreateTransactionOutput
from domain.entities.transaction import Transaction, TransactionType
from domain.exceptions import AccountNotFoundError
from domain.repositories.account_repository import AccountRepository
from domain.repositories.transaction_repository import TransactionRepository


class CreateTransactionUseCase:
    def __init__(
        self,
        account_repository: AccountRepository,
        transaction_repository: TransactionRepository,
    ):
        self._account_repo = account_repository
        self._transaction_repo = transaction_repository

    async def execute(self, input_data: CreateTransactionInput) -> CreateTransactionOutput:
        account = await self._account_repo.get_by_id(input_data.account_id)
        if account is None:
            raise AccountNotFoundError(f"Conta {input_data.account_id} não encontrada")

        # a regra de negócio mora na entidade — o use case só chama
        if input_data.type == TransactionType.EXPENSE:
            account.withdraw(input_data.amount)
        else:
            account.deposit(input_data.amount)

        transaction = Transaction(
            account_id=input_data.account_id,
            amount=input_data.amount,
            type=input_data.type,
            category=input_data.category,
            description=input_data.description,
        )

        await self._transaction_repo.save(transaction)
        await self._account_repo.save(account)

        return CreateTransactionOutput(
            transaction_id=transaction.id,
            new_balance=account.balance,
        )
