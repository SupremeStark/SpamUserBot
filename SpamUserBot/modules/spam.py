import asyncio
from SpamUserBot import PREFIXES
from SpamUserBot.steve.funcs import custom_handler
from pyrogram.errors import FloodWait 

async def _spam(client, message):
    mod_use = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴀᴍ>\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ>\n\ncᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ."
    err_msg = "sᴘᴀᴍ Mᴏᴅᴜʟᴇ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ᴛɪʟʟ 𝟷𝟶𝟶 ᴄᴏᴜɴᴛ. Fᴏʀ ʙɪɢɢᴇʀ sᴘᴀᴍs ᴜsᴇ BɪɢSᴘᴀᴍ"
    try:
        await message.delete()
    except:
        pass
    replied = message.reply_to_message

    if message.text[0].isalpha() and message.text[0] in PREFIXES :
        await message.reply_text(mod_use)

    if len(message.command) == 1:
        await message.reply_text(mod_use)

    replied = message.reply_to_message
    text = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 1)
    if text[0].isdigit():
        num = int(text[0]) 
    else:
        await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")
    if len(text) == 2:
        to_spam = str(text[1])
        if num > 100:
            await message.reply_text(err_msg)
        for i in range(num):
            try:
                await client.send_message(message.chat.id,to_spam)
            except FloodWait as m:
                await asyncio.sleep(m.value)
    if replied and replied.photo:
        photo = replied.photo.file_id              
        if not replied.caption:
            txt = None
        txt = replied.caption
        if num > 100:
            await message.reply_text(err_msg)
        for i in range(num):
            try:
                await client.send_photo(message.chat.id,photo=photo, caption=txt) 
            except FloodWait as m:
                await asyncio.sleep(m.value)  
             
        
        

custom_handler("spam",_spam)
