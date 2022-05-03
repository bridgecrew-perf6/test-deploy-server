from fastapi import APIRouter

router = APIRouter()


@router.get(path='/isActive')
async def is_active():
    return True


@router.get(path='/ping')
async def ping():
    return 'pong'