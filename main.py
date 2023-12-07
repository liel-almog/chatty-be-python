import asyncio

from hypercorn.asyncio import serve
import hypercorn

from server import server


async def app(scope, receive, send):
    await server.app(scope, receive, send)


async def main():
    hypercorn_config = hypercorn.Config()
    hypercorn_config.bind = ["localhost:8080"]
    hypercorn_config.use_reloader = True
    await serve(app, hypercorn_config)


if __name__ == "__main__":
    asyncio.run(main())
