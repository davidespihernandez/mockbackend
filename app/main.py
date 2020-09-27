from fastapi import FastAPI

from .routers import operators

app = FastAPI()


app.include_router(
    operators.router,
    prefix="/sp/api/v13/user/operators",
    tags=["operators"],
    responses={404: {"description": "Not found"}},
)