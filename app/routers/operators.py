from fastapi import APIRouter

from app.modules.mockers.operators import OperatorsMocker


router = APIRouter()
mocker = OperatorsMocker()


@router.get("/")
async def read_operators():
    return mocker.get_list()


@router.get("/{operator_id}")
async def read_operator(operator_id: str):
    return mocker.get_detail(operator_id)
