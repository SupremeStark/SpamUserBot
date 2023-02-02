from SpamUserBot.steve.funcs import custom_handler



def _abuse(client, message):
    try:
        await message.delete()
    except:
        pass
    if len(message.command) == 1:
        return await message.reply_text("**Mᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴀʙᴜsᴇ**\n\nCᴏᴍᴍᴀɴᴅ:\n\n .ɢᴀʟɪ <ᴜsᴇʀ ʜᴀɴᴅʟᴇʀ>\n\nɪᴛ ᴡɪʟʟ ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ ᴀʙᴜsᴇ ᴜɴᴛɪʟ ʏᴏᴜ ʀᴇsᴛᴀʀᴛ!!.")
    user = 
