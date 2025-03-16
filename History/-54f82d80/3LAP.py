import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
	bot = Bot(token='7913468169:AAFYSYAOQUPYVe3hgMFermzBjt9UStE0_rg')
	dp = Dispatcher()
	dp.include_router(router)
	await dp.start_polling(bot)
     
if __name__ == '__main__':
	asyncio.run(main())