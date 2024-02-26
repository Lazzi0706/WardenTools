from fastapi import APIRouter

router = APIRouter()

@router.get("/spacelawcalc/")
async def get_page():
    pass