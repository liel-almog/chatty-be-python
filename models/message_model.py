from datetime import datetime
from pydantic import BaseModel, Field


class MessageModel(BaseModel):
    id: int
    room_id: int = Field(serialization_alias="roomId", alias="roomId")
    username: str
    content: str
    created_at: datetime = Field(serialization_alias="createdAt", alias="createdAt")

class CreateMessageModel(BaseModel):
    room_id: int = Field(serialization_alias="roomId", alias="roomId")
    username: str
    content: str
