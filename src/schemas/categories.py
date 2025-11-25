from pydantic import BaseModel
from .base_response import BaseResponse


class CategoryResponse(BaseResponse):
    title: str
    slug: str = None
    icon: str = None


class CategorySchema(BaseModel):
    title: str
    icon: str = None
