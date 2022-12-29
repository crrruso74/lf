from translation import *
from config import UPDATE_CHANNEL, WELCOME_IMAGE
from pyrogram import Client, filters
from plugins.database import collection
from pymongo import TEXT
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    collection.create_index([("title" , TEXT),("caption", TEXT)],name="movie_index")
    if len(m.command) == 1:
        return await m.reply_photo(WELCOME_IMAGE,
            caption=START_MESSAGE.format(m.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 🤖", url=f'https://t.me/{UPDATE_CHANNEL')
                    ]
                ]
            )
        )
    else:
        return await group_send_handler(c,m)

