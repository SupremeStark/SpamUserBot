import asyncio
from SpamUserBot.modules.cancel import SPAM_CHATS
from SpamUserBot.steve.funcs import custom_handler
from SpamUserBot.steve.strings import RAID
from pyrogram.errors import FloodWait 

async def _raid(client, message):
    try:
        await message.delete()
    except:
        pass
    if len(message.command) == 1:
        await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.ʀᴀɪᴅ <ᴜsᴇʀ ʜᴀɴᴅʟᴇʀ>\n\nᴄᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ.")
    text = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 1)
    chat_id = message.chat.id
    SPAM_CHATS.append(chat_id)
    if len(text) == 2:
        user = str(text[1])
        mm = await client.get_users(user)
        name = mm.first_name
        id = mm.id
        mention = f"[{name}](tg://user?id={id})"        
        
        print(name)
        count = int(text[0]) if text[0].isdigit() else await message.reply("𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ.")
        print(count)
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
