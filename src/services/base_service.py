
import shutil
import uuid

from fastapi import UploadFile, HTTPException
from pathlib import Path

from core.settings import settings


class BaseService:

    @staticmethod
    async def upload_image(file: UploadFile, image_path: str):
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Only image files allowed")

        media_dir: Path = settings.media_path / image_path
        media_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{uuid.uuid4().hex}_{file.filename}"
        file_path = media_dir / filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"image_path": f"/media/{image_path}/{filename}"}
