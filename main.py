import asyncio
from typing import Union
from fastapi import FastAPI
import uvicorn
import utils.env 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

async def main():
    config = uvicorn.Config("main:app", port=8080, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
