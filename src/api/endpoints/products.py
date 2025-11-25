import logging
from typing import List
from fastapi import APIRouter, Request
from sqlalchemy.orm import selectinload

from repositories.produсts import ProductRepository, ProductGalleryRepository, ProductCharacteristicsRepository, BrandRepository
from repositories.categories import CategoryRepository
from schemas.products import (
    BrandSchema, BrandResponse,
    ProductSchema, ProductResponse,
    ProductGallerySchema, ProductGalleryResponse,
    CharacteristicsSchema, CharacteristicsResponse
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter(
    tags=["Page"],
    responses={404: {"description": "Not found"}},
)


@router.get('/brands', response_model=List[BrandResponse])
async def get_brands(request: Request):
    db = request.state.db
    brand_repo = BrandRepository(db)
    brands = await brand_repo.get_all()
    return brands


@router.post('/brands', response_model=BrandResponse)
async def create_brand(request: Request, data: BrandSchema):
    db = request.state.db
    product_data  = data.dict()
    brand_repo = BrandRepository(db)
    brand = await brand_repo.create_data(product_data)
    return brand


@router.get('/products', response_model=List[ProductResponse])
async def get_products(request: Request):
    db = request.state.db
    product_repo = ProductRepository(db)
    products = await product_repo.get_all(
        selectinload(product_repo.model.characteristics),
        selectinload(product_repo.model.gallery),
        selectinload(product_repo.model.categories),
        selectinload(product_repo.model.brand)
    )
    return products


@router.post('/products', response_model=ProductResponse)
async def create_product(request: Request, data: ProductSchema):
    db = request.state.db
    product_repo = ProductRepository(db)
    product_gallery_repo = ProductGalleryRepository(db)
    product_characteristics_repo = ProductCharacteristicsRepository(db)
    category_repo = CategoryRepository(db)
    product_data = data.dict()
    gallery_data = product_data.pop('product_gallery')
    characteristics_data = product_data.pop('characteristics')
    categories_objects = await category_repo.get_by_ids(product_data.pop('categories'))
    product_data['categories'] = categories_objects
    product = await product_repo.create_data(product_data)
    if product:
        for file in gallery_data:
            file.update({"product_id": product.id})
            await product_gallery_repo.create_data(file)
        for characteristics in characteristics_data:
            characteristics.update({"product_id": product.id})
            await product_characteristics_repo.create_data(characteristics)

    reloaded_product = await product_repo.get_data_by_id(
        product.id,
        selectinload(product_repo.model.characteristics),
        selectinload(product_repo.model.gallery),
        selectinload(product_repo.model.categories),
        selectinload(product_repo.model.brand)
    )

    return reloaded_product


@router.get('/products/photos/{product_id}', response_model=List[ProductGalleryResponse])
async def get_gallery_product(request: Request, product_id: int):
    db = request.state.db
    # product_repo = ProductRepository(db)
    product_gallery_repo = ProductGalleryRepository(db)
    # product = await product_repo.get_data_by_id(product_id)
    product_gallery = await product_gallery_repo.get_by_id_product(product_id)
    return product_gallery
