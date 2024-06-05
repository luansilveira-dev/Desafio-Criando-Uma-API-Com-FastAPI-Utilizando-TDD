from datetime import datetime, timezone
from uuid import uuid4
from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    