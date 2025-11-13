import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
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
    return templates.TemplateResponse(
        request=request, name="index.html"
    )


@router.get("/product", response_class=HTMLResponse)
async def product_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="product.html"
    )
