
from pyrogram import Client, filters
from pyrogram.types import Message
from .database import collection
from config import ADMINS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Add Movie to database
@Client.on_message(filters.user(ADMINS) & filters.media & filters.private)
async def web_db(c: Client, m: Message):
    if m.caption and m.photo:
        is_exist = collection.find_one({"unique_id": m.photo.file_unique_id,  "caption": m.caption.html})

        if is_exist:  
          return await m.reply("This file already exist")
          
        message = m.caption
      

        id = collection.insert_one(
            {
                "caption": message.html,
                "title": message.splitlines()[0],
                "unique_id": m.photo.file_unique_id,
                "thumbnail": m.photo.file_id,
            }
        )

        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Delete", callback_data=f"delete#{id.inserted_id }"
                    )
                ],
            ]
        )

        await m.reply("Added Successfully", reply_markup=reply_markup)

    else:
        await m.reply("Something went wrong")
