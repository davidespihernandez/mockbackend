from typing import List, Dict

from fastapi import HTTPException
from pydantic import BaseModel


class Mocker:
    objects: Dict[int, BaseModel] = dict()

    def __init__(self, objects):
        self.objects = objects

    def get_detail(self, object_id: int) -> BaseModel:
        try:
            return self.objects[object_id]
        except KeyError:
            raise HTTPException(status_code=404)

    def get_list(self) -> List[BaseModel]:
        return [v for k, v in self.objects.items()]
