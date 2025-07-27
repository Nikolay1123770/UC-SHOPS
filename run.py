from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio
from bot import start_bot  # импортируем запуск бота из bot.py

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    # Запускаем бота в фоне при старте FastAPI
    asyncio.create_task(start_bot())


@app.get("/")
def read_root():
    return {"status": "ok", "message": "UC SHOP API запущен."}


@app.get("/privacy-policy")
def privacy_policy():
    return FileResponse("html/privacy-policy.html", media_type="text/html")


@app.get("/terms-of-service")
def terms_of_service():
    return FileResponse("html/terms-of-service.html", media_type="text/html")
