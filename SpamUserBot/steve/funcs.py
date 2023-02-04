from pyrogram.handlers import MessageHandler
from SpamUserBot import PREFIXES , SUDO_USERS,UB,UB2,UB3,UB4,UB5
from pyrogram import filters 


def custom_handler(cmd,func):
    try:
        UB.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
        UB2.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
        UB3.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
        UB4.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
        UB5.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
    except Exception as a:
        print(a)



async def get_user_id(message, text:str):
    def is_int(text : str):
        try:
            int(text)
        except ValueError:
            return False
        return True
    
    text = text.strip()
    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == MessageEntityType.MENTION:
        return (await app.get_users(text)).id
    if entity.type == MessageEntityType.TEXT_MENTION:
        return entity.user.id
    return None

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
