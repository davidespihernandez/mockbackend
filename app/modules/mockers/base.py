from typing import Dict

from fastapi import HTTPException
from pydantic import BaseModel

from app.modules.models.base import ListOfModels


class Mocker:
    objects: Dict[str, BaseModel] = dict()

    def get_detail(self, object_id: str) -> BaseModel:
        try:
            return self.objects[object_id]
        except KeyError:
            raise HTTPException(status_code=404)

    def get_list(self) -> ListOfModels:
        return ListOfModels(objects=[v for k, v in self.objects.items()])
