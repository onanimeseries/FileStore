#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Ｓａｔｕｒｏ</a>\n○ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/OnAnimeSeries'>ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ</a>\n○ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋs : <a href='https://t.me/OnAnimeSeries_Network'>ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ ɴᴇᴛᴡᴏʀᴋ</a>\n○ ꜱᴜᴘᴘᴏʀᴛ : <a href='https://t.me/OnAnimeseriesSupport'>ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ ꜱᴜᴘᴘᴏʀᴛ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/OnAnimeseriesUniverse'>ᴀɴɪᴍᴇ ᴜɴɪᴠᴇʀꜱᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴄʜᴀɴɴᴇʟ ', url='https://t.me/OnAnimeSeries')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

