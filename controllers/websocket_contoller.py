import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from models.message_model import CreateMessageModel
from services.message_service import CommonMessageService

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, list[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_id: int):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

    def disconnect(self, websocket: WebSocket, room_id: int):
        self.active_connections[room_id].remove(websocket)

    async def broadcast(self, room_id: int, message: str):
        active_connections = self.active_connections.get(room_id)

        if active_connections:
            for connection in active_connections:
                await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/chat/{room_id}")
async def websocket_endpoint(
    websocket: WebSocket, room_id: int, message_service: CommonMessageService
):
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_text()
            message_json = json.loads(data)
            create_message = CreateMessageModel(**message_json)
            message = await message_service.create(create_message)
            await manager.broadcast(room_id, message.model_dump_json(by_alias=True))
    except WebSocketDisconnect:
        manager.disconnect(websocket, room_id)
