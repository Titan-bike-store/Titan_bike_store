import logging
from typing import List

from fastapi import APIRouter, Request
from schemas.categories import CategoryCreateSchema, CategoryResponse
from repositories.categories import CategoryRepository
from services.base_service import BaseService


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/categories",
    tags=["Page"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(lambda: None)]
)


@router.get("/", response_model=List[CategoryResponse])
async def get_categories(request: Request):
    db = request.state.db
    category_repo = CategoryRepository(db)
    category = await category_repo.get_all()
    return category


@router.post("/", response_model=CategoryResponse)
async def create_category(category_data: CategoryCreateSchema, request: Request):
    db = request.state.db

    update_data = category_data.dict(exclude_unset=True)

    if category_data.icon:
        image_info = await BaseService.upload_image(category_data.icon, "avatars")
        update_data["icon"] = image_info['image_path']

    category_repo = CategoryRepository(db)
    category = await category_repo.create_data(update_data)

    return category
