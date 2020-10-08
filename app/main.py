from fastapi import FastAPI

from .routers import operators, users, redirect

app = FastAPI()


app.include_router(
    operators.router,
    prefix="/api/operators",
    tags=["operators"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    users.router,
    prefix="/api/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# default router for any other request, will be redirected to a "real"
# test server, which allows to start mocking only some things
app.include_router(
    redirect.router,
    prefix="/api",
    tags=["redirect"],
    responses={404: {"description": "Not found"}},
)
