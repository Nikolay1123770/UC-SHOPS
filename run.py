import asyncio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from threading import Thread
from bot import main as bot_main  # импортируем из bot.py

app = FastAPI()

@app.get("/privacy-policy")
async def privacy():
    return FileResponse("html/privacy-policy.html", media_type="text/html")

@app.get("/terms-of-service")
async def terms():
    return FileResponse("html/terms-of-service.html", media_type="text/html")

def start_fastapi():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

def start_bot():
    asyncio.run(bot_main())

if __name__ == "__main__":
    Thread(target=start_fastapi).start()
    Thread(target=start_bot).start()

import asyncio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from threading import Thread
from bot import main as bot_main  # импортируем из bot.py

app = FastAPI()

@app.get("/privacy-policy")
async def privacy():
    return FileResponse("html/privacy-policy.html", media_type="text/html")

@app.get("/terms-of-service")
async def terms():
    return FileResponse("html/terms-of-service.html", media_type="text/html")

def start_fastapi():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

def start_bot():
    asyncio.run(bot_main())

if __name__ == "__main__":
    Thread(target=start_fastapi).start()
    Thread(target=start_bot).start()
