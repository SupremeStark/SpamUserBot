import asyncio
import random 
from SpamUserBot.modules.cancel import SPAM_CHATS
from SpamUserBot.steve.funcs import custom_handler , extract_user_id
from SpamUserBot.steve.strings import RAID
from pyrogram.errors import FloodWait 

async def _raid(client, message):
    try:
        await message.delete()
    except:
        pass
    user_id = await extract_user_id(message)
    if len(message.command) == 1:
        await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.ʀᴀɪᴅ <ᴜsᴇʀ ʜᴀɴᴅʟᴇʀ>\n\nᴄᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ.")
    if not user_id:
        return await message.reply_text("**ᴍᴇɴᴛɪᴏɴ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ**")
    text = message.text.split()
    print(text)
    chat_id = message.chat.id
    SPAM_CHATS.append(chat_id)
    if len(text) >= 2:
        if text[1].isdigit():
            count = int(text[1])  
        else:
            await message.reply("𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ.")
        mm = await client.get_users(user_id)
        name = mm.first_name
        mention = f"[{name}](tg://user?id={user_id})"                        
        for ok in range(count):
            GALI = random.choice(RAID)
            msg = f"{mention} {GALI}"
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_message(chat_id,msg) 
            except FloodWait as e:
                  print(e)
                  await asyncio.sleep(e.value) 
    

custom_handler("raid",_raid)
