from SpamUserBot.modules.cancel import SPAM_CHATS
from SpamUserBot.steve.funcs import custom_handler

async def _raid(client, message):
    try:
        await message.delete()
    except:
        pass
    if len(message.command) == 1:
        await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.ʀᴀɪᴅ <ᴜsᴇʀ ʜᴀɴᴅʟᴇʀ>\n\nᴄᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ.")
    text = message.command
    if len(text) == 2:
        count = int(text[1]) if text[1].isdigit() else await message.reply("
    

custom_handler("raid",_raid)
