from fastapi import APIRouter

router = APIRouter()

@router.get("/home/")
async def get_page():
    pass