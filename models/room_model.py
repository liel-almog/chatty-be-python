from pydantic import BaseModel, Field
from datetime import datetime

class RoomModel(BaseModel):
    id: int
    name: str = Field(min_length=1)
    created_at: datetime
