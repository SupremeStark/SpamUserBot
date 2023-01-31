import os
from pyrogram import Client
from SpamUserBot import LOG

LOG.print("[bold cyan]☮▁▂▃▄☾ ♛ Text ♛ ☽▄▃▂▁☮")

HII = """
███░░███░░███
███░░███░░░░░
███░░███░░███
███▄▄███░░███
████████░░███
███▀▀███░░███
███░░███░░███
███░░███░░███
███░░███░░███
"""

LOG.print(f"[bold cyan]{HII}")

APP_ID = int(input("\nEnter APP ID here: "))
API_HASH = input("\nEnter API HASH here: ")


try :
    with Client("Session",api_id = API_ID,api_hash=API_HASH) as steve :
        s = await steve.export_session_string()
        LOG.print("[bold yellow]sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʏʀᴏɢʀᴀᴍ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ.")
        await steve.send_message("me",s)
        LOG.print("[bold yellow]ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇ.")

except Exception as er:
    LOG.print("[bold red]{er}")
