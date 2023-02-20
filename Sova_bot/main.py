from aiogram.utils import executor
from config import bot, dp 
import logging
from handlers import klient, callback, extra, admin, fsm_anketa
from datebase.bot_db import sql_create

klient.register_handlers_klient(dp)
callback.regisetr_handler_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)

extra.register_handlers_extra(dp)

async def table_start(_):
    sql_create()

if __name__== "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, table_start=table_start)