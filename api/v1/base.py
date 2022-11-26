from fastapi import APIRouter

api_v1_router = APIRouter(
    prefix='/api/v1',
    tags=['api_v1'],
    dependencies=[],
)


@api_v1_router.get('/ping')
async def ping() -> str:
    return 'pong'
