from fastapi import APIRouter
from .room import router as room_router

api_router = APIRouter()
api_router.include_router(room_router, prefix="/room")