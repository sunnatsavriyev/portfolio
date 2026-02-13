from django.core.management.base import BaseCommand
import asyncio
from home.bot import dp, bot

class Command(BaseCommand):
    help = "Run Telegram Bot"

    def handle(self, *args, **kwargs):
        self.stdout.write("🤖 Telegram bot ishga tushdi")
        asyncio.run(dp.start_polling(bot))
