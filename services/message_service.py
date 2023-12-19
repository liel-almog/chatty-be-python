from typing import Annotated
from databases import Database
from fastapi import Depends
from database.db import CommonDB
from models.message_model import CreateMessageModel, MessageModel


class MessageService:
    def __init__(self, db: Database):
        self.db = db

    async def get_all_by_room(self, room_id: int):
        return await self.db.fetch_all(
            "SELECT id, room_id, content, created_at, username FROM public.messages WHERE room_id = :room_id",
            values={"room_id": room_id},
        )

    async def create(self, message: CreateMessageModel):
        [id, room_id, content, created_at, username] = await self.db.execute(
            "INSERT INTO public.messages (room_id, content, username) VALUES (:room_id, :content, :username) RETURNING (id, room_id, content, created_at, username)",
            values={
                "room_id": message.room_id,
                "content": message.content,
                "username": message.username,
            },
        )

        return MessageModel(
            id=id,
            room_id=room_id,
            content=content,
            username=username,
            created_at=created_at,
        )


def get_message_service(db: CommonDB):
    return MessageService(db)


CommonMessageService = Annotated[
    MessageService, Depends(get_message_service, use_cache=True)
]
