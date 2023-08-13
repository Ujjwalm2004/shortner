from pyrogram import Client, filters
from database import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(filters.command('start'))
async def start(_, m):
    await m.reply_photo(
        photo=PIC,
        chat_id=int(m.from_user.id),
        caption=START_TEXT.format(m.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                 InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                [InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/Cyber_Url"),
                 InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/cyberstock_support")],
                [InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")]
            ]
        )
    )


