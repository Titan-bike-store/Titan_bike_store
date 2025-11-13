from fastapi import APIRouter

from .endpoints.views import router as views_router


router = APIRouter()
router_list = [
    views_router,
]

for r in router_list:
    router.include_router(r)
