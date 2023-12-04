from enum import Enum
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from controllers import api_router
from errors import validation
import uvicorn


app = FastAPI()
app.include_router(api_router, prefix="/api")
app.add_exception_handler(
    RequestValidationError, validation.validation_exception_handler
)


async def serve():
    config = uvicorn.Config("main:app", port=8080, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()
