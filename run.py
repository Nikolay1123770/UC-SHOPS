from fastapi import FastAPI
import uvicorn
import asyncio

from start_bot import main as start_bot_main  # Импорт функции запуска бота

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "UC SHOP is running"}


# Запуск бота параллельно с сервером FastAPI
@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot_main())
