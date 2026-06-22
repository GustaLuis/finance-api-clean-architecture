from pydantic import BaseModel, Field
from decimal import Decimal
from uuid import UUID

class CreateAccountRequest(BaseModel):
    user_id: UUID
    name: str
    initial_balance: Decimal = Field(default=Decimal("0"), ge=0)

class CreateAccountResponse(BaseModel):
    account_id: UUID
    name: str
    balance: Decimal

class AccountResponse(BaseModel):
    account_id: UUID
    user_id: UUID
    name: str
    balance: Decimal