from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from database.users import *
from handlers.handlers import *
from configs import *
import asyncio


@Client.on_message(filters.command('start') & filters.private)
async def start(_, m):
    await handle_private_message(client, message)

    text = message.text
    cmd = text.split("_", 1)[-1]

    if cmd == "/start":
        try:
         #   bot = await Client.get_me()
            await m.reply_text(
                #photo=PIC,
                START_TXT.format(m.from_user.mention), #bot.mention),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                         InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                        [InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/Cyber_Url"),
                         InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/cyberurl_support")],
                        [InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")]
                    ]
                )
            )


@Client.on_message(filters.command('set_api') & filters.private)
async def set_api(c, m):
    n = await m.reply_text("Pʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    u_api = await db.get_api(m.from_user.id)
    if u_api:
        await n.edit(f"Yᴏᴜʀ ᴀᴩᴜ {u_api}")
    if len(m.command) == 1:
       return await m.reply_text("**Gɪᴠᴇ ᴍᴇ ʏᴏᴜʀ ᴀᴩɪ ᴡɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ**\n\n**Exᴀᴍᴩʟᴇ - /set_api ᴀᴩɪ**\n\n**Gᴇᴛ ʏᴏᴜʀ ᴀᴩɪ ᴋᴇʏ [ʜᴇʀᴇ](https://cyberurl.in/member/tools/api)**")
    user_id = m.from_user.id
    api = m.text.split(' ', 1)[1]
    await db.set_api(m.from_user.id, api=api)
    await m.reply_text(f'**API ᴋᴇʏ sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\n**Yᴏʏʀ API: `{api}`**')

