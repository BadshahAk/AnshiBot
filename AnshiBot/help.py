# AnshiBot/help.py

async def help_cmd(client, message):
    await message.reply(
        "**Anshi Help Menu**\n\n"
        "- `/start` : Radhe Radhe bolne wali entry\n"
        "- `/help` : Yehi message\n"
        "- `/joke` : Suno ek mazedaar chutkula\n"
        "- `/shayri` : Thodi pyaari si shayri\n\n"
        "*Note:* Main gandi baatein aur stickers hata deti hu!"
    )
