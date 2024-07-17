from pyrogram import Client
import asyncio


with Client:
    app_username = Client.get_me().username
    
async def reply(update, copied):
    msg_id = copied.id
    media_types = [copied.video, copied.photo, copied.audio, copied.document, copied.sticker, copied.animation, copied.voice, copied.video_note]
    for media_type in media_types:
        if media_type:
            unique_idx = media_type.file_unique_id
            break
    await update.reply_text(
        '**لینک اشتراک فایل شما:\n\n**'
        f"`https://t.me/{app_username}?start={unique_idx.lower()}-{str(msg_id)}`",
        True,
    )
    await asyncio.sleep(0.5)