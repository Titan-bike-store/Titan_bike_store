from fastapi import APIRouter

from .endpoints.views import router as views_router
from .endpoints.category import router as views_category


router = APIRouter()
router_list = [
    views_router,
    views_category
]

for r in router_list:
    router.include_router(r)
