from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    title: str
    slug: str = None
    icon: str = None


class CategoryCreateSchema(BaseModel):
    title: str
    icon: str = None
