from databases import Database
from database.db import CommonDB


class MessageService:
    def __init__(self, db: Database):
        self.db = db

    async def get_all_by_room(self, room_id: int):
        return await self.db.fetch_one(
            "SELECT id, room_id, content, created_at, username FROM public.messages WHERE room_id = :room_id",
            values={"room_id": room_id},
        )


def get_message_service(db: CommonDB):
    return MessageService(db)
