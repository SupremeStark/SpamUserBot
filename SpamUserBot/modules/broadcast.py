from SpamUserBot.steve.funcs import custom_handler
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait 

async def _broadcast(client, message):
    try:
        message.delete()
    except:
        pass 
    text =  await message.reply("`ɢᴇᴛᴛɪɴɢ ᴀʟʟ ᴄʜᴀᴛs ɪᴅ....`)
    replied = message.reply_to_message
    chats = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.SUPERGROUP,ChatType.GROUP,ChatType.PRIVATE]:
            chats.append(dialog.chat.id)
    await text.edit("`ɢᴏᴛ {len(chats)} ᴄʜᴀᴛs. ɴᴏᴡ sᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ.......`")
    if replied:
        x = message.reply_to_message.id
        y = message.chat.id
        sent = 0
        for i in chats:
            try:
                m = await client.forward_messages(i, y, x)                
                sent += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception:
                pass
        return await text.edit(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")
        
    elif len(message.command) < 2:
        return await text.edit("**ᴇxᴀᴍᴩʟᴇ :**\n/broadcast [ᴍᴇssᴀɢᴇ] ᴏʀ [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]")       
    else:
        text = message.text.split(None, 1)[1]
        sent = 0   
        for i in chats:
            try:
                m = await client.send_message(i, text=text)           
                sent += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception:
                pass
        return await text.edit(f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")


custom_handler(["broadcast","bcast"],_broadcast)
