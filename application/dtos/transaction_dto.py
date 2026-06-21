from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from domain.entities.transaction import TransactionType


@dataclass
class CreateTransactionInput:
    account_id: UUID
    amount: Decimal
    type: TransactionType
    category: str
    description: str


@dataclass
class CreateTransactionOutput:
    transaction_id: UUID
    new_balance: Decimal
