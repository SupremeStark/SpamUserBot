from SpamUserBot.steve.funcs import custom_handler,extract_user_id , get_user_id



async def _abuse(client, message):
    try:
        await message.delete()
    except:
        pass
    print(await extract_user_id(message))
    if len(message.command) == 1:
        return await message.reply_text("**Mᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴀʙᴜsᴇ**\n\nCᴏᴍᴍᴀɴᴅ:\n\n .ɢᴀʟɪ <ᴜsᴇʀ ʜᴀɴᴅʟᴇʀ>\n\nɪᴛ ᴡɪʟʟ ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ ᴀʙᴜsᴇ ᴜɴᴛɪʟ ʏᴏᴜ ʀᴇsᴛᴀʀᴛ!!.")
    

custom_handler("abuse",_abuse)
