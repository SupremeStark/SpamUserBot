from SpamUserBot.steve.funcs import custom_handler
from pyrogram.enums import ChatType


async def _broadcast(client, message):
    chats = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type 
