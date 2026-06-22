from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class CreateAccountInput:
    user_id: UUID
    name: str
    initial_balance: Decimal = Decimal("0")


@dataclass
class CreateAccountOutput:
    account_id: UUID
    name: str
    balance: Decimal


@dataclass
class AccountOutput:
    account_id: UUID
    user_id: UUID
    name: str
    balance: Decimal