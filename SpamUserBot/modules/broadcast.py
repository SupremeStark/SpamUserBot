from SpamUserBot.steve.funcs import custom_handler
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait 

async def _broadcast(client, message):
    chats = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.SUPERGROUP,ChatType.GROUP,ChatType.PRIVATE]:
            chats.append(dialog.chat.id)
    if message.reply_to_message:
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
        await message.reply_text(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")
        return
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
    return await message.reply_text(f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")


custom_handler(["broadcast","bcast"],_broadcast)
