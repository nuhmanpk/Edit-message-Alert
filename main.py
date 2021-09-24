import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "BotNameHere",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@bughunter0.on_message(filters.edited)
async def edited(bot,message):
	chatid= message.chat.id	
	await bot.send_message(text=f"{message.from_user.mention} Edited This [Message]({message.link})",chat_id=chatid)
	
bughunter0.run()