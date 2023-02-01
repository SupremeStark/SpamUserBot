import asyncio
import importlib

from pyrogram import idle , filters , Client 
from SpamUserBot import LOG ,SUDO_USERS
from SpamUserBot.modules import ALL_MODULES

loop = asyncio.get_event_loop()

async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("SpamUserBot.modules." + all_module)
    LOG.print("[bold yellow]ɴᴏᴡ ᴀᴍ ʀᴇᴀᴅʏ ᴛᴏ ғɪɢʜᴛ ʙᴏss..")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄᴇʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")


@Client.on_message(filters.command("start", prefixes = ["."]) & (filters.me | filters.user(SUDO_USERS)))
async def _start(_, message):
    await message.reply_text("ok working")

if __name__ == "__main__":
    loop.run_until_complete(start_bot())
    
