from datetime import datetime
from pydantic import BaseModel


class BaseResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
