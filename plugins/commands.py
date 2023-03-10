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
                        InlineKeyboardButton("π€ ππΏπ³π°ππ΄π π€", url=f'https://t.me/MX_Networks')
                    ]
                ]
            )
        )
    else:
        return await group_send_handler(c,m)

