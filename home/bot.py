# home/bot.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from .models import Murojaat
from asgiref.sync import sync_to_async


API_TOKEN = "8351295778:AAHObNWtDHLRm_YpX_pdv23JCoEt8BYqTXI"
ADMIN_IDS = [1948824452]

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📩 Umumiy murojaatlar")]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Admin panel", reply_markup=menu)

@sync_to_async
def get_murojaatlar():
    return list(Murojaat.objects.order_by("-created_at")[:10])

@dp.message(lambda m: m.text == "📩 Umumiy murojaatlar")
async def all(msg: Message):
    data = await get_murojaatlar()

    if not data:
        await msg.answer("Hozircha yo‘q")
        return

    text = ""
    for m in data:
        text += f"👤{m.firstname} {m.lastname}\n📝{m.murojaat}\n\n"

    await msg.answer(text)