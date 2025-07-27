from start_bot import main as start_bot_main
import asyncio

asyncio.create_task(start_bot_main())

async def handler(request):
    return {
        "statusCode": 200,
        "body": "UC SHOP bot is running!"
    }
