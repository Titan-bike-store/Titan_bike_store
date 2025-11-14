import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from sqladmin import Admin

from starlette.middleware.cors import CORSMiddleware

from middleware.auth_middleware import AuthMiddleware
from middleware.db_middleware import DBSessionMiddleware
from api.routers import router as api_router
from core.settings import settings
from core.db import db_instance
# from admin.views.users import UserAdmin
# from admin.views.categories import CategoryAdmin
# from admin.views.products import BrandAdmin, ProductAdmin, ProductGalleryAdmin, CharacteristicsAdmin


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_instance.create_database()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version="0.0.1",
    lifespan=lifespan,
)

if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.mount("/media", StaticFiles(directory=settings.media_path), name="media")
app.mount("/static", StaticFiles(directory=settings.static_path), name="static")
app.mount("/vendor", StaticFiles(directory=settings.static_vendor_path), name="vendor")
app.mount("/js",     StaticFiles(directory=settings.static_js_path),     name="js")
app.mount("/images", StaticFiles(directory=settings.static_images_path), name="images")
templates = Jinja2Templates(directory="templates")

app.add_middleware(AuthMiddleware)
app.add_middleware(DBSessionMiddleware, session_factory=db_instance._async_session_maker)
app.include_router(api_router)

# admin.add_view(UserAdmin)
# admin.add_view(CategoryAdmin)
# admin.add_view(BrandAdmin)
# admin.add_view(ProductAdmin)
# admin.add_view(ProductGalleryAdmin)
# admin.add_view(CharacteristicsAdmin)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True,
                workers=1, limit_concurrency=100, limit_max_requests=1000)
