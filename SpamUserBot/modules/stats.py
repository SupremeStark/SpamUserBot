from SpamUserBot.steve.funcs import custom_handler
from pyrogram.enums import ChatType

async def _stats(client, message):
    try:
        await message.delete()
    except:
        pass
    text = await message.reply("`ᴘʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs......`")
    users = 0
    bots = 0
    groups = 0
    channels = 0    
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:            
            users += 1
        elif dialog.chat.type in [ChatType.SUPERGROUP,ChatType.GROUP]:
            groups += 1
        elif dialog.chat.type == ChatType.CHANNEL :
            channels += 1
        elif dialog.chat.type == ChatType.BOT :
            bots += 1
    done = "💖 ʜᴇʀᴇ's ᴍɪɴᴇ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs....\n\n"
    done += f"**⦾ ʙᴏᴛs :** {bots}\n"
    done += f"**⦾ ᴜsᴇʀs :** {users}\n"
    done += f"**⦾ ɢʀᴏᴜᴘs :** {groups}\n"
    done += f"**⦾ ᴄʜᴀɴɴᴇʟs :** {channels}\n"
    await text.edit(done)


custom_handler("stats",_stats)

        
    
