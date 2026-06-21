from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from domain.entities.transaction import TransactionType


class CreateTransactionRequest(BaseModel):
    account_id: UUID
    amount: Decimal = Field(gt=0)
    type: TransactionType
    category: str
    description: str = ""


class CreateTransactionResponse(BaseModel):
    transaction_id: UUID
    new_balance: Decimal
