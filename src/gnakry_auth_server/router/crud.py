from fastapi import APIRouter

router = APIRouter()


@router.get("/posts")
async def posts():
    return {"posts": 'test'}


@router.get("/user/me", tags=["users"])
async def read_user_me():
    return {"username": "simple user"}
