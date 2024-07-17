from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os 
from dotenv import load_dotenv,dotenv_values # type: ignore

load_dotenv()

START_BUTTONS = [
    [
        InlineKeyboardButton(
            'گیت هاب', url='https://github.com/Milaadmg023'),
        InlineKeyboardButton('کانال', url='https://t.me/MD_Dev1'),
    ],
    [InlineKeyboardButton('سازنده', url="https://t.me/M_B21")],
]

TRACK_CHANNEL = os.getenv('TRACK_CHANNEL')

@Client.on_message(filters.command('start') & filters.private)
async def start_file(bot, update):
    if update.text == '/start':
        await update.reply_text(
            "سلام به ربات اشتراک گذاری فایل خوش اومدید💕\nشما میتوانید هر فایلی که دلتون بخواد رو برای من بفرستید و لینک اون فایل رو دریافت کنید🤖\n\nبرای اطلاعات بیشتر /help رو ارسال کنید👀",
            True, reply_markup=InlineKeyboardMarkup(START_BUTTONS))
        return

    if len(update.command) != 2:
        return
    code = update.command[1]
    if '-' in code:
        msg_id = code.split('-')[-1]
        unique_id = '-'.join(code.split('-')[0:-1])

        if not msg_id.isdigit():
            return
        try:
            check_media_group = await bot.get_media_group(TRACK_CHANNEL, int(msg_id))
            check = check_media_group[0]
        except Exception:
            check = await bot.get_messages(TRACK_CHANNEL, int(msg_id))

        if check.empty:
            await update.reply_text('Error: [Message does not exist]\n/help for more details...')
            return
        media_types = [check.video, check.photo, check.audio, check.document, check.sticker, check.animation, check.voice, check.video_note]
        for media_type in media_types:
            if media_type:
                unique_idx = media_type.file_unique_id
                break
        if unique_id != unique_idx.lower():
            return
        try:
            await bot.copy_media_group(update.from_user.id, TRACK_CHANNEL, int(msg_id))
        except Exception:
            await check.copy(update.from_user.id)
    else:
        return
