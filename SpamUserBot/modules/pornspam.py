import random 
import asyncio
from SpamUserBot.modules.cancel import SPAM_CHATS
from SpamUserBot.steve.funcs import custom_handler , extract_user_id
from pyrogram.errors import FloodWait
from SpamUserBot.steve.strings import PORN

async def _pornspam(client, message):
    try:
        await message.delete()
    except:
        pass
    user_id = await extract_user_id(message)
    if len(message.command) <= 1:
        await message.reply_text("**ᴘᴏʀɴsᴘᴀᴍ ᴜsᴀɢᴇ :**\n\n.ᴘᴏʀɴsᴘᴀᴍ < ᴄᴏᴜɴᴛ > <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>")
    if not user_id:
        await message.reply_text("ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ")
    count = message.command[1]
    chat_id = message.chat.id
    SPAM_CHATS.append(chat_id)
    print(count)
    mention = (await client.get_users(user_id)).mention 
    for _ in range(count):
        if chat_id not in SPAM_CHATS:
            break
        porm = random.choice(PORN)
        try:
            await client.send_video(chat_id,video=porm)
        except FloodWait as e:
            await asyncio.sleep(e.value)

custom_handler("pornspam",_pornspam)
