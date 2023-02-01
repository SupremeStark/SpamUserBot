from SpamUserBot.steve.funcs import custom_handler

async def _spam(client, message):
    mod_use = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\ɴ\ɴᴄᴏᴍᴍᴀɴᴅ:\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴀᴍ>\n\n.sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ>\n\ncᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ."
    err_msg = "sᴘᴀᴍ Mᴏᴅᴜʟᴇ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ᴛɪʟʟ 𝟷𝟶𝟶 ᴄᴏᴜɴᴛ. Fᴏʀ ʙɪɢɢᴇʀ sᴘᴀᴍs ᴜsᴇ BɪɢSᴘᴀᴍ"
    try:
        await message.delete()
    except:
        pass
    replied = message.reply_to_message
    if not replied or len(message.command) < 2:
        await message.reply_text(mod_use)


custom_handler("spam",_spam)
