from fastapi import APIRouter

from .endpoints.views import router as views_router
from .endpoints.categories import router as category_router
from .endpoints.products import router as product_router


router = APIRouter()
router_list = [
    views_router,
    category_router,
    product_router
]

for r in router_list:
    router.include_router(r)
