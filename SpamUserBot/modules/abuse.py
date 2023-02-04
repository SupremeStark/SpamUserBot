import asyncio
from SpamUserBot.steve.funcs import custom_handler,extract_user_id , get_user_id
from pyrogram.errors import FloodWait
from SpamUserBot.modules.cancel import SPAM_CHATS


async def _abuse(client, message):
    try:
        await message.delete()
    except:
        pass
    user_id = await extract_user_id(message)
    if len(message.command) == 1:
        return await message.reply_text("**Mᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴀʙᴜsᴇ**\n\nCᴏᴍᴍᴀɴᴅ:\n\n .ɢᴀʟɪ <ᴜsᴇʀ ʜᴀɴᴅʟᴇʀ>.")
    if not user_id:
        return await message.reply_text("**ᴍᴇɴᴛɪᴏɴ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ**")
    user = await client.get_users(user_id)
    user_name = user.first_name or user.last_name
    name = f"[{user_name}](tg://user?id={user_id})"
    chat_id = message.chat.id
    if user_id == 5505555398:
        return await message.reply_text("ʙsᴅᴋ ᴍᴀᴅᴀʀᴄʜᴏᴅ ʙᴇʜᴇɴᴄʜᴏᴅ ᴡᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜ 😂😂")
    SPAM_CHATS.append(chat_id)
    GALI = [
        f"{name} GAND FATT GYII KYA HIJRE KI OLAAD",
        f"{name} **RANDI KE PILLLE**",
        f"{name} 𝑪𝑯𝑯𝑯𝑯𝑯𝑼𝑼𝑼𝑼𝑼𝑫𝑫𝑫𝑫 𝑮𝒀𝑨𝑨𝑨𝑨𝑨𝑨𝑨 𝑳𝑶𝑽𝑽𝑽𝑽𝑽𝑫𝑫𝑬𝑬 𝑻𝑼𝑼𝑼𝑼",
        f"{name} 𝕋𝕖𝕣𝕚 𝕄𝕒𝕒 𝕂𝕚 𝕏𝕙𝕠𝕥 𝕓𝕒𝕕𝕙𝕧𝕖",
        f"{name} **ISKE MAAKI CHUTT LELO FREE FULL NIGHT**",
        f" {name} __TERE MAAKI CHUTT MASTT SOFT SOFT HE__ 🤤",
        f"# {name} TERE MAAKI CHUT ME MERAA LUNDD",
        f"{name} **RAANDD KAA PILLAAA**",
        f"{name} 𝙄𝙎𝙆𝙄 𝘽𝙃𝙀𝙉 𝙈𝙀𝙍𝘼 𝙇𝙐𝙉𝘿 𝘾𝙃𝙊𝙊𝙎𝙏𝙄𝙄 𝙃E",
        f"{name} __AGAYA SWADH__",
        f"{name} **TERI MAAA**",
        "**MERE SE**",
        "**Rozz CHUDTII**",
        "__Haiii__",
        f"{name} TERE BHEN KO CHODU",
        "🆃🅰🅿🅰",
        "🆃🅰🅿",
        "🆃🅰🅿🅰",
        "🆃🅰🅿",
        "__NON STOP__",
        f"{name} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗘 𝗟𝗨𝗡𝗗 𝗟𝗘 𝗡𝗔𝗖𝗛𝗧𝗜 𝗛𝗘",
        "🤤",
        f"{name} __TERI MAA MST ARAAM DETI HE__🤤🤤",
        f"{name} __KE BHEN KI CHUT LELO FULL NIGHT FREEE__",
        f"{name} __KI BHEN RANDIII__",
        f"{name} __ISKE BHEN MST MARI RANDI__ 🤤🤤",
        "😂🖕🤣",
        "😂",
        f"__EK RUPAY KI PEPSI {name} KI NAANI SEXYY__",
        f"{name} **ISKI BHEN MERI PERSONAL HE MENE BOHOT CHODAA HE USKO__ \n\n __DM {name} FOR PERSONAL RANDI__",
    ]
    for mc in GALI:
        if chat_id not in SPAM_CHATS:
            break
        try:
            await client.send_message(chat_id,mc)
            await asyncio.sleep(0.3)
        except FloodWait as i:
            await asyncio.sleep(i.value)
    try :
        SPAM_CHATS.remove(chat_id)
    except Exception:
        pass


custom_handler("abuse",_abuse)
