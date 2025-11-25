from typing import List
from datetime import datetime
from pydantic import BaseModel
from .base_response import BaseResponse
from .categories import CategoryResponse


class BrandSchema(BaseModel):
    title: str
    icon: str


class BrandResponse(BaseResponse):
    title: str
    slug: str | None
    icon: str | None


class ProductGallerySchema(BaseModel):
    file: str


class ProductGalleryResponse(BaseResponse):
    # product_id: int
    file: str


class CharacteristicsSchema(BaseModel):
    name: str
    value: str


class CharacteristicsResponse(BaseResponse):
    name: str
    value: str


class ProductSchema(BaseModel):
    title: str
    description: str
    price: int
    quantity: int
    brand_id: int | None
    categories: List[int] = []
    product_gallery: List[ProductGallerySchema] = []
    characteristics: List[CharacteristicsSchema] = []


class ProductResponse(BaseResponse):
    title: str
    description: str
    price: int
    quantity: int
    brand: BrandResponse = None
    categories: List[CategoryResponse] = []
    gallery: List[ProductGalleryResponse] = []
    characteristics: List[CharacteristicsResponse] = []
