from SpamUserBot import PREFIXES
from SpamUserBot.steve.funcs import custom_handler

async def _spam(client, message):
    mod_use = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴀᴍ>\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ>\n\ncᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ."
    err_msg = "sᴘᴀᴍ Mᴏᴅᴜʟᴇ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ᴛɪʟʟ 𝟷𝟶𝟶 ᴄᴏᴜɴᴛ. Fᴏʀ ʙɪɢɢᴇʀ sᴘᴀᴍs ᴜsᴇ BɪɢSᴘᴀᴍ"
    try:
        await message.delete()
    except:
        pass
    replied = message.reply_to_message

    if message.text[0].isalpha() and message.text[0] in PREFIXES :
        await message.reply(mod_use)
    Deadly = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 1)
    print(Deadly)

custom_handler("spam",_spam)
