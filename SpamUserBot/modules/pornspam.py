import random 
import asyncio
from SpamUserBot.modules.cancel import SPAM_CHATS
from SpamUserBot.steve.funcs import custom_handler
from pyrogram.errors import FloodWait
from SpamUserBot.steve.strings import PORN

async def _pornspam(client, message):
    try:
        await message.delete()
    except:
        pass
    if len(message.command) <= 1:
        await message.reply_text("**ᴘᴏʀɴsᴘᴀᴍ ᴜsᴀɢᴇ :**\n\n.ᴘᴏʀɴsᴘᴀᴍ < ᴄᴏᴜɴᴛ >")
    count = int(message.command[1]) if message.command[1].isdigit() else await message.reply_text("𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ.")
    
    chat_id = message.chat.id
    SPAM_CHATS.append(chat_id)    
    for _ in range(count):
        if chat_id not in SPAM_CHATS:
            break
        porm = random.choice(PORN)
        try:
            await client.send_video(chat_id,video=porm)
        except FloodWait as e:
            await asyncio.sleep(e.value)

custom_handler("pornspam",_pornspam)
