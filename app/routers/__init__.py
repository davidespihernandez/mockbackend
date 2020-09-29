from fastapi import Header


async def auth_header(authorization: str = Header(...)):
    return authorization.removeprefix("Token ")
