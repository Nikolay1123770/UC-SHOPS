import asyncio
import uvicorn
from app.bot import start_bot
from app.server import app

async def main():
    bot_task = asyncio.create_task(start_bot())

    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    server_task = asyncio.create_task(server.serve())

    await asyncio.gather(bot_task, server_task)

if __name__ == "__main__":
    asyncio.run(main())
