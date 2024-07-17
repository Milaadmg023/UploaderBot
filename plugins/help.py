from pyrogram import Client, filters

@Client.on_message(filters.command('help') & filters.private)
async def help_message(bot, update):
    await update.reply_text("فرمت های پشتیبانی شده ربات:\n\n- Video\n- Audio\n- Photo\n- Document\n- Sticker\n- GIF\n- Voice note\n- Video note\n\n در صورت بروز مشکل به ایدی @M_B21 پیام بدهید", True)