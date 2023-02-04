import os
import time
import sys
import asyncio
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from SpamUserBot.steve.strings import LOG_MSG ,EMOJI

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
SESSION = Config.SESSION
SESSION2 = Config.SESSION2
PREFIXES = Config.PREFIXES
SUDO_USERS = Config.SUDO_USERS

#rich
LOG = Console()

#time
StartTime = time.time()
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

async def SpamUserBot():
    global BOT
    global UB
    global UB2    
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(LOG_MSG)
    LOG.print(header)
    LOG.print(f"[bold green]{EMOJI}")
    if TOKEN:
        BOT = Client("BotHun",api_id = API_ID,api_hash = API_HASH,bot_token=TOKEN,in_memory=True)
        await BOT.start()
        LOG.print("[bold yellow]💝 ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ......")
        LOG.print("[bold orange]🔥ɴᴏᴡ ʙᴏᴏᴛɪɴɢ ᴄʟɪᴇɴᴛs.....")
    else:
        LOG.print("[bold red]ʙᴏᴛ ᴛᴏᴋᴇɴ ɴᴏᴛ ғᴏᴜɴᴅ ᴇxɪsᴛɪɴɢ......")
        sys.exit(1) 

    if SESSION:
        try:
            UB = Client("SESSION",api_id = API_ID,api_hash = API_HASH, session_string = SESSION)
            LOG.print("[bold cyan]ɢᴏᴛᴄʜᴀ sᴇssɪᴏɴ 𝟷")
            await UB.start()
            ub = await UB.get_me()
            await UB.join_chat("Steve_Projects")
            await UB.join_chat("Testing_support_group")
            SUDO_USERS.append(ub.id)
            LOG.print("[bold yellow]✨ sᴇssɪᴏɴ 𝟷 sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")
        except Exception as idk:
            LOG.print(f"[bold red]{idk}")
    else:
        LOG.print("[bold red]sᴇssɪᴏɴ𝟷 ɴᴏᴛ ғᴏᴜɴᴅ")
        UB = None
      
    if SESSION2:
        try:
            UB2 = Client("SESSION2",api_id = API_ID,api_hash = API_HASH, session_string = SESSION2)
            LOG.print("[bold cyan]ɢᴏᴛᴄʜᴀ sᴇssɪᴏɴ 2")
            await UB2.start()
            ub2 = await UB2.get_me()
            await UB2.join_chat("Steve_Projects")
            await UB2.join_chat("Testing_support_group")
            SUDO_USERS.append(ub2.id)
            LOG.print("[bold yellow]✨ sᴇssɪᴏɴ 2 sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")
        except Exception as idk:
            LOG.print(f"[bold red]{idk}")
    else:
        LOG.print("[bold red]sᴇssɪᴏɴ2 ɴᴏᴛ ғᴏᴜɴᴅ")
        UB2 = None

    

loop = asyncio.get_event_loop()
loop.run_until_complete(SpamUserBot())    



    
    

    
    



