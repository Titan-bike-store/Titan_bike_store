import logging
from sqlalchemy.orm import selectinload

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from repositories.produсts import ProductRepository
from repositories.categories import CategoryRepository

from core.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory=settings.templates_path)


router = APIRouter(
    tags=["Page"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(lambda: None)]
)


@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    db = request.state.db
    products_repo = ProductRepository(db)
    categories_repo = CategoryRepository(db)
    categories = await categories_repo.get_all()
    products = await products_repo.get_all(
        selectinload(products_repo.model.brand),
        selectinload(products_repo.model.characteristics),
        selectinload(products_repo.model.gallery),
        selectinload(products_repo.model.categories)
    )
    return templates.TemplateResponse(
        request=request, name="index.html", context={
            "products": products,
            "categories": categories
        }
    )


@router.get("/product", response_class=HTMLResponse)
async def product_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="product.html"
    )
