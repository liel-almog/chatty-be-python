import asyncio
from server import server
from dotenv import load_dotenv

async def app(scope, receive, send):
    await server.app(scope, receive, send)

async def main():
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
