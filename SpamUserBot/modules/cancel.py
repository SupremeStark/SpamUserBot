from SpamUserBot.steve.funcs import custom_handler

SPAM_CHATS = []

async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("sᴛᴏᴘᴘᴇᴅ ᴛʜᴇ ᴘʀᴏᴄᴇss.")     
                                     
    else :
        await message.reply_text("**ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴇss ɢᴏɪɴɢ ᴏɴ ʙᴀʙʏ.**")  
        return       


custom_handler(["cancel","stop"],cancelcmd)
