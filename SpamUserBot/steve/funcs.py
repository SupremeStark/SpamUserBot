from pyrogram.handlers import MessageHandler
from SpamUserBot import UB, UB2 , PREFIXES

def custom_handler(cmd,func):
    UB.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
    UB2.add_handler(MessageHandler(func, filters.command(cmd,PREFIXES) & filters.user(SUDO_USERS)))
