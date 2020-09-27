from pydantic import BaseModel


class Operator(BaseModel):
    id: int
    uid: str
    name: str
