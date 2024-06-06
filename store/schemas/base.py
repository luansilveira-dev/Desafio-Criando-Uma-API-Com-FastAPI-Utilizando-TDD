from datetime import datetime, timezone
from uuid import uuid4
from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True
    