from fastapi import APIRouter


router = APIRouter(prefix="/api")
router_list = [
]

for r in router_list:
    router.include_router(r)
