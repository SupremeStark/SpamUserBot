from SpamUserBot.modules.cancel import SPAM_CHATS
from SpamUserBot.steve.funcs import custom_handler

async def _raid(client, message):
    try:
        await message.delete()
    except:
        pass
    if len(message.command) == 1:
        await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.ʀᴀɪᴅ <ᴜsᴇʀ ʜᴀɴᴅʟᴇʀ>\n\nᴄᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ.")
    text = message.text.split()
    text.pop(0)
    print(text)
    if len(text) == 2:
        user = str(text[1])
        try:
            mm = await client.get_users(user)
        except Exception as e:
            print(e)
        name = mm.first_name
        id = mm.id
        mention = f"[{name}](tg://user?id={id})"
        
        count = int(text[0]) if text[0].isdigit() else await message.reply("𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ.")
        print(count)
    

custom_handler("raid",_raid)
