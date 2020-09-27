from fastapi import APIRouter

from app.modules.mockers.operators import OperatorsMocker
from app.modules.data.operators import objects


router = APIRouter()
mocker = OperatorsMocker(objects=objects)


@router.get("/")
async def read_operators():
    return mocker.get_list()


@router.get("/{item_id}")
async def read_operator(item_id: int):
    return mocker.get_detail(item_id)
