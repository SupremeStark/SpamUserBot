import asyncio
import importlib

from pyrogram import idle , filters , Client 
from SpamUserBot import LOG ,SUDO_USERS  , UB, UB2
from SpamUserBot.modules import ALL_MODULES
from pyrogram.handlers import MessageHandler
from SpamUserBot.steve.funcs import custom_handler
from SpamUserBot.steve.strings import START_TEXT
from pyrogram import __version__ as idk

loop = asyncio.get_event_loop()

async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("SpamUserBot.modules." + all_module)
    LOG.print("[bold yellow]ɴᴏᴡ ᴀᴍ ʀᴇᴀᴅʏ ᴛᴏ ғɪɢʜᴛ ʙᴏss..")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄᴇʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")



async def _start(client, message):
    me = (await client.get_me()).mention
    await message.delete()
    msg = await message.reply("⚡")
    await asyncio.sleep(1.5)
    await msg.delete()
    await message.reply_photo(
        photo = "https://graph.org/file/3e390f9f1e3c71ee5b394.jpg",
        caption = START_TEXT.format(me,idk))


custom_handler(["start","alive"],_start)

if __name__ == "__main__":
    loop.run_until_complete(start_bot())
    
