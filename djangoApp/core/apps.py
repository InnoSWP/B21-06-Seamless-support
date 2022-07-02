import asyncio
from threading import Thread

from aiogram.utils import executor
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        print('Running core app...')
        from core.telegram import dp

        import signal

        def run():

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            executor.start_polling(dp, skip_updates=True, reset_webhook=True)

        def stop(*args):
            dp.stop_polling()

        print('Running bot...')
        bot_thread = Thread(target=run)
        bot_thread.start()

        signal.signal(signal.SIGINT, stop)

