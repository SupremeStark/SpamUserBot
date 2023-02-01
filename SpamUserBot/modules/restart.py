import os
from SpamUserBot.steve.funcs import custom_handler


async def _restart(client, message):
    try:
        await message.delete()
    except:
        pass
    text = await message.reply("🎣 sᴛᴀʀᴛɪɴɢ ᴀ ɴᴇᴡ ɪɴsᴛᴀɴᴄᴇ ᴀɴᴅ sʜᴜᴛᴛɪɴɢ ᴅᴏᴡɴ ᴛʜɪs ᴏɴᴇ.......")    
    try:
        os.system(f"kill -9 {os.getpid()} && python3 -m SpamUserBot")
    except Exception as er:
        print(er)
    

custom_handler("restart",_restart)
