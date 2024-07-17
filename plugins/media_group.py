from pyrogram import Client,filters
import os
from dotenv import load_dotenv , dotenv_values # type: ignore

load_dotenv()

OWNER_ID = os.getenv('OWNER_ID')
TRACK_CHANNEL = os.getenv('TRACK_CHANNEL')

# Store media group
media_group_id = 0

@Client.on_message(filters.media & filters.private & filters.media_group)
async def store_media_group(bot, update):
    global media_group_id
    if OWNER_ID == 'all' or int(OWNER_ID) == update.from_user.id:
        if int(media_group_id) != int(update.media_group_id):
            media_group_id = update.media_group_id
            copied = (await bot.copy_media_group(TRACK_CHANNEL, update.from_user.id, update.id))[0]
            await bot.reply(update, copied)
    else:
        return

@Client.on_message(filters.media & filters.private & ~filters.media_group)
async def store_media(bot, update):
    if OWNER_ID == 'all' or int(OWNER_ID) == update.from_user.id:
        copied = await update.copy(TRACK_CHANNEL)
        await bot.reply(update, copied)