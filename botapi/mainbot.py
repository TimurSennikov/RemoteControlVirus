from .bot import *
from .dispatcher import *
from .handlers import *

async def run_bot_service():
    await dp.start_polling(bot)