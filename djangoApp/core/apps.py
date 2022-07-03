from threading import Thread

from django.apps import AppConfig
import asyncio


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'Core'

    def ready(self):
        from core.telegram import bot
        import signal

        def run():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            bot.infinity_polling()

        def stop(*args):
            bot.stop_polling()

        print('Running bot...')
        bot_thread = Thread(target=run)
        bot_thread.start()

        signal.signal(signal.SIGINT, stop)
