# AnshiBot/start.py

from config import OWNER_ID, START_IMG_URL
from pyrogram.types import Message

async def start_cmd(client, message: Message):
    await message.reply_photo(
        photo=START_IMG_URL,
        caption=(
            "Radhe Radhe!\n\n"
            "Main *Anshi* hu, ek 5 saal ki pyaari si sanskaari bacchi!\n"
            "Main aap se baatein karungi, jokes sunaoongi, aur ganda content hataoongi!"
        )
    )
