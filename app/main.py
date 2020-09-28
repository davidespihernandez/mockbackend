from fastapi import FastAPI

from .routers import operators, users

app = FastAPI()


app.include_router(
    operators.router,
    prefix="/sp/api/v13/user/operators",
    tags=["operators"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    users.router,
    prefix="/sp/api/v13",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
