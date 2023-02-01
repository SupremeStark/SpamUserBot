from pyrogram.hanlders import MessageHandler
from SpamUserBot import UB, UB2

def custom_handler(cmd,func):
    UB.add_handler(MessageHandler(func, filters.command(cmd,prefixes = ["."]) & filters.user(SUDO_USERS)))
    UB2.add_handler(MessageHandler(func, filters.command(cmd,prefixes = ["."]) & filters.user(SUDO_USERS)))
