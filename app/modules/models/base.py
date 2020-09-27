from typing import Optional, List

from pydantic import BaseModel, HttpUrl


class ListOfModels(BaseModel):
    count: int
    next: Optional[HttpUrl]
    previous: Optional[HttpUrl]
    results: List[BaseModel]

    def __init__(self, objects: List[BaseModel]):
        super().__init__(
            count=len(objects),
            next=None,
            previous=None,
            results=objects,
        )
