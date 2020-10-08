import requests

from typing import Optional

from fastapi import APIRouter, Header, Response


router = APIRouter()


@router.get("/{path:path}")
async def request_anything(
    path: str,
    authorization: Optional[str] = Header(None),
):
    url = "https://real.server.url/api/" + path
    headers = {
        "Authorization": authorization,
    }
    r = requests.get(url, headers=headers)
    return Response(status_code=r.status_code, content=r.content)
