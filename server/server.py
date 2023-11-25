from fastapi import FastAPI
from controllers import api_router
import uvicorn

app = FastAPI()
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "ass"}

async def serve():
    config = uvicorn.Config("main:app", port=8080, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

