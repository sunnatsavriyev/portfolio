# home/bot.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from asgiref.sync import database_sync_to_async
from .models import Murojaat

API_TOKEN = "8351295778:AAHObNWtDHLRm_YpX_pdv23JCoEt8BYqTXI"
ADMIN_IDS = [1948824452,5079701692]  # kerak bo'lsa boshqa adminlarni qo'shing

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Keyboard
menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📩 Umumiy murojaatlar")]],
    resize_keyboard=True
)

# Start command
@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Admin panel", reply_markup=menu)

# Async ORM query
@database_sync_to_async
def get_murojaatlar():
    return list(Murojaat.objects.order_by("-created_at")[:10])

# Umumiy murojaatlar handler
@dp.message(Text(text="📩 Umumiy murojaatlar"))
async def all_murojaatlar(msg: Message):
    data = await get_murojaatlar()

    if not data:
        await msg.answer("Hozircha yo‘q")
        return

    text = ""
    for m in data:
        text += (
            f"👤 {m.firstname} {m.lastname}\n"
            f"📝 {m.murojaat}\n"
            f"⏰ {m.created_at.strftime('%d-%m-%Y %H:%M')}\n\n"
        )

    await msg.answer(text)

# Funksiya: murojaat kelganda adminlarga yuborish
@database_sync_to_async
def send_to_admins(text: str):
    import requests

    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    for admin in ADMIN_IDS:
        try:
            requests.post(
                url,
                json={
                    "chat_id": admin,
                    "text": text,
                    "parse_mode": "Markdown"
                },
                timeout=5
            )
        except Exception as e:
            print("Telegram error:", e)

# Run bot
def run_bot():
    print("🤖 Telegram bot ishga tushdi...")
    asyncio.run(dp.start_polling())
