from aiogram.utils import executor
from create import dp
from handler import user
from handler.user import asyncio


user.register_handlers(dp)






executor.start_polling(dp, skip_updates=True)