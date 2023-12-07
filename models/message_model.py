from datetime import datetime
from pydantic import BaseModel


class MessageModel(BaseModel):
    id: int
    room_id: int
    user_id: int
    content: str
    created_at: datetime
