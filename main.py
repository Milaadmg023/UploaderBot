from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import os
from dotenv import load_dotenv, dotenv_values  # type: ignore

plugins = dict(root="plugins")


load_dotenv()

# Configurations
API_HASH = os.getenv('API_HASH')
APP_ID = os.getenv('APP_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')
TRACK_CHANNEL = os.getenv('TRACK_CHANNEL')
OWNER_ID = os.getenv('OWNER_ID')


# Initialize bot
app = Client('File-Sharing', api_id=APP_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=plugins)

with app:
    app_username = app.get_me().username
    print("bot is online...")


app.run()