from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from application.dtos.account_dto import CreateAccountInput
from application.use_cases.create_account import CreateAccountUseCase
from application.use_cases.get_account import GetAccountUseCase
from application.use_cases.list_accounts import ListAccountsUseCase
from domain.exceptions import AccountNotFoundError

from ..dependencies import (
    get_create_account_use_case,
    get_get_account_use_case,
    get_list_accounts_use_case,
)
from ..schemas.account_schema import (
    CreateAccountRequest,
    CreateAccountResponse,
    AccountResponse,
)

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("/", response_model=CreateAccountResponse, status_code=201)
async def create_account(
    request: CreateAccountRequest,
    use_case: CreateAccountUseCase = Depends(get_create_account_use_case),
):
    input_data = CreateAccountInput(
        user_id=request.user_id,
        name=request.name,
        initial_balance=request.initial_balance,
    )
    output = await use_case.execute(input_data)
    return CreateAccountResponse(
        account_id=output.account_id,
        name=output.name,
        balance=output.balance,
    )


@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(
    account_id: UUID,
    use_case: GetAccountUseCase = Depends(get_get_account_use_case),
):
    try: 
        output = await use_case.execute(account_id)
    except AccountNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    return AccountResponse(**output.__dict__)


@router.get("/", response_model=list[AccountResponse])
async def list_accounts(
    user_id: UUID,
    use_case: ListAccountsUseCase = Depends(get_list_accounts_use_case),
):
    outputs = await use_case.execute(user_id)
    return [AccountResponse(**output.__dict__) for output in outputs]