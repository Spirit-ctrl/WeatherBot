import asyncio
import logging
import sys

from settings import get_bot_token
from routers.start.router import start_router
from bd import engine, Base
from aiogram import Bot, Dispatcher


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main() -> None:
    # Initialize bot and dispatcher on the active event loop
    bot = Bot(token=get_bot_token())
    dp = Dispatcher()
    dp.include_router(start_router)

    # Prepare DB (run within the same event loop)
    await init_models()

    try:
        await dp.start_polling(bot)
    finally:
        # Ensure bot's session is closed when stopping
        await bot.session.close()


if __name__ == "__main__":
    print("Bot is starting...")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user")

