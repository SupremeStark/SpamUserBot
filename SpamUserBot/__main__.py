import asyncio
import importlib

from pyrogram import idle , filters , Client 
from SpamUserBot import LOG ,SUDO_USERS  , UB, UB2
from SpamUserBot.modules import ALL_MODULES
from pyrogram.handlers import MessageHandler


loop = asyncio.get_event_loop()

async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("SpamUserBot.modules." + all_module)
    LOG.print("[bold yellow]ɴᴏᴡ ᴀᴍ ʀᴇᴀᴅʏ ᴛᴏ ғɪɢʜᴛ ʙᴏss..")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄᴇʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")



async def _start(_, message):
    await message.reply_text("ok working")

def cumtom_handler(cmd,func):
    UB.add_handler(MessageHandler(func, filters.command(cmd,prefixex = ["."]) & filters.user(SUDO_USERS)))
    UB2.add_handler(MessageHandler(func, filters.command(cmd,prefixex = ["."]) & filters.user(SUDO_USERS)))

custom_handler(_start,"start")

if __name__ == "__main__":
    loop.run_until_complete(start_bot())
    
