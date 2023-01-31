import os
from pyrogram import Client
from SpamUserBot import LOG

os.system("clear")

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

API_ID = int(input("\nEnter APP ID here: "))
API_HASH = input("\nEnter API HASH here: ")


try :
    with Client("Session",api_id = API_ID,api_hash=API_HASH) as steve :
        steve.storage.SESSION_STRING_FORMAT=">B?256sQ?"
        s = steve.export_session_string()
        LOG.print("[bold yellow]sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʏʀᴏɢʀᴀᴍ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ.")
        steve.send_message("me",s)
        LOG.print("[bold yellow]ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇ.")

except Exception as er:
    LOG.print(f"[bold red]{er}")
