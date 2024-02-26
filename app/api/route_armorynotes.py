from fastapi import APIRouter

router = APIRouter()

@router.get("/armorynotes/")
async def get_page():
    pass