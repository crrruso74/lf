import ast
import re
from pyrogram import Client, filters
from pyrogram.types import Message
from .database import collection
from config import *
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)



@Client.on_message(filters.chat(CHANNELS_LIST) & filters.media & filters.channel & filters.incoming)
async def channel_movie_handler(c: Client, m: Message):
    if CHANNELS == "True":
        if m.caption and m.photo:
            message = m.caption
          
            if collection.find_one({"unique_id": m.photo.file_unique_id,  "caption": message.html}):  
              return 
          
            id = collection.insert_one(
                {"caption": message.html,
                'title': message.splitlines()[0],
                 'thumbnail':m.photo.file_id,
                 "unique_id": m.photo.file_unique_id, 
                }
            )

            reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Delete", callback_data=f"delete#{id.inserted_id }")],
            ])
            txt = await c.send_message(
                chat_id=OWNER_ID,
                text=f"Post Added Successfully\n\nPost Link: [Click]({m.link})",
                reply_markup=reply_markup,
                disable_web_page_preview=True
            )
        else:
            txt = await c.send_message(
                chat_id=OWNER_ID,
                text=f"Something went wrong on adding post \n\nPost Link: [Click]({m.id})",
                reply_markup=reply_markup,
                disable_web_page_preview=True
            )
