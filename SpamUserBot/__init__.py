import os
import time
import asyncio
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from SpamUserBot.steve.string import LOG_MSG ,EMOJI

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
SUDO_USERS = Config.SUDO_USERS
SESSION = Config.SESSION

#rich
LOG = Console()

#time
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

#client
UB  = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    session_string = SESSION )
    



async def SpamUserBot():
    global UB
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(LOG_MSG)
    LOG.print(header)
    LOG.print("[bold yellow]ɢᴇᴛᴛɪɴɢ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ.....")
    
    await asyncio.sleep(2)
    LOG.print("[bold yellow]ɢᴏᴛ ᴀʟʟ ᴛʜᴇ ɪɴғᴏ......")
    await asyncio.sleep(1)
    

loop = asyncio.get_event_loop()
#loop.run_until_complete(SpamUserBot())    



    
    

    
    



