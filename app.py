from fastapi import FastAPI
from starlette.responses import RedirectResponse

from config import APPLICATION_NAME

application = FastAPI(
    title=APPLICATION_NAME,
)


@application.get('/ping')
async def ping() -> str:
    return 'ping works'


@application.get('/', include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    response = RedirectResponse(url='/docs')
    return response


def build_app() -> FastAPI:
    from api.v1.base import api_v1_router

    # include routers
    application.include_router(api_v1_router)

    return application
