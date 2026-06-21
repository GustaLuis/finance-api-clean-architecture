from fastapi import APIRouter, Depends, HTTPException

from application.dtos.transaction_dto import CreateTransactionInput
from application.use_cases.create_transaction import CreateTransactionUseCase
from domain.exceptions import AccountNotFoundError, InsufficientFundsError

from ..dependencies import get_create_transaction_use_case
from ..schemas.transaction_schema import CreateTransactionRequest, CreateTransactionResponse

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/", response_model=CreateTransactionResponse, status_code=201)
async def create_transaction(
    request: CreateTransactionRequest,
    use_case: CreateTransactionUseCase = Depends(get_create_transaction_use_case),
):
    input_data = CreateTransactionInput(
        account_id=request.account_id,
        amount=request.amount,
        type=request.type,
        category=request.category,
        description=request.description,
    )

    try:
        output = await use_case.execute(input_data)
    except AccountNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except InsufficientFundsError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return CreateTransactionResponse(
        transaction_id=output.transaction_id,
        new_balance=output.new_balance,
    )
