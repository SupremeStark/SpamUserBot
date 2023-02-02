import asyncio
from SpamUserBot import PREFIXES
from SpamUserBot.steve.funcs import custom_handler
from pyrogram.errors import FloodWait 

SPAM_CHATS = []



async def _spam(client, message):
    mod_use = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴀᴍ>\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ>\n\ncᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ."
    err_msg = "sᴘᴀᴍ Mᴏᴅᴜʟᴇ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ᴛɪʟʟ 𝟷𝟶𝟶 ᴄᴏᴜɴᴛ."
    try:
        await message.delete()
    except:
        pass
    replied = message.reply_to_message
    chat_id = message.chat.id
    SPAM_CHATS.appned(chat_id)
    if len(message.command) == 1  :
        await message.reply_text(mod_use)     
    replied = message.reply_to_message
    text = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 1)    
    if len(text) == 2:
        if text[0].isdigit():
            num = int(text[0]) 
        else:
            await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")
        to_spam = str(text[1])
        for i in range(num):
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_message(message.chat.id,to_spam)
            except FloodWait as m:
                await asyncio.sleep(m.value)
    if replied and replied.photo:
        photo = replied.photo.file_id 
        if text[0].isdigit():
            num = int(text[0]) 
        else:
            await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")             
        if not replied.caption:
            txt = None
        txt = replied.caption        
        for i in range(num):
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_photo(message.chat.id,photo=photo, caption=txt) 
            except FloodWait as m:
                await asyncio.sleep(m.value)  
             
    if replied and replied.video:
        video = replied.video.file_id 
        if text[0].isdigit():
            num = int(text[0]) 
        else:
            await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")             
        if not replied.caption:
            txt = None
        txt = replied.caption
        for i in range(num):
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_video(message.chat.id,video=video, caption=txt) 
            except FloodWait as m:
                await asyncio.sleep(m.value)  
                     
    if replied and replied.document:
        doc = replied.document.file_id 
        if text[0].isdigit():
            num = int(text[0]) 
        else:
            await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")             
        if not replied.caption:
            txt = None
        txt = replied.caption
        for i in range(num):
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_document(message.chat.id,doc, caption=txt) 
            except FloodWait as m:
                await asyncio.sleep(m.value)  
                     
    if replied and replied.sticker:
        sticker = replied.sticker.file_id 
        if text[0].isdigit():
            num = int(text[0]) 
        else:
            await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")             
        for i in range(num):
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_sticker(message.chat.id,sticker) 
            except FloodWait as m:
                await asyncio.sleep(m.value)  


    if replied and replied.animation:
        file = replied.animation.file_id
        if text[0].isdigit():
            num = int(text[0]) 
        else:
            await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")             
        if not replied.caption:
            txt = None
        txt = replied.caption
        for i in range(num):
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_animation(message.chat.id, animation = file, caption=txt) 
            except FloodWait as m:
                await asyncio.sleep(m.value)  
                                                          
    if replied and replied.text:
        msg = replied.text 
        if text[0].isdigit():
            num = int(text[0]) 
        else:
            await message.reply_text("**𝟸ɴᴅ ᴀʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ**")                     
        for i in range(num):
            if chat_id not in SPAM_CHATS:
                break
            try:
                await client.send_message(message.chat.id,msg) 
            except FloodWait as m:
                await asyncio.sleep(m.value)  
                             

custom_handler("spam",_spam)
