from pyrogram.handlers import MessageHandler
from SpamUserBot import UB, UB2 , PREFIXES , SUDO_USERS
from pyrogram import filters 


def custom_handler(cmd,func):
    UB.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
    UB2.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))



async def get_id_reason_or_rank(message,sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    replied = message.reply_to_message
    if replied:
                
        if not replied.from_user:
            if (
                    replied.sender_chat
                    and replied.sender_chat != message.chat.id
                    and sender_chat
            ):
                id_ = replied.sender_chat.id
            else:
                return None, None
        else:
            id_ = replied.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason
    
    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await get_user_id(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await get_user_id(message, user), reason

    return user, reason

async def extract_user_id(message):    
    return (await get_id_reason_or_rank(message))[0]
