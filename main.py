import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import router as handler_router


async def main():

    bot = Bot('7177932019:AAEpQxuvDU0Q8jfaOag2kTvrFRzTZbsa8Wc')

    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    dp.include_router(router=handler_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
