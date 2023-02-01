import time 
from SpamUserBot.steve.funcs import custom_handler
from SpamUserBot import get_readable_time, StartTime


async def _ping(client, message):
    await message.delete()
    start = time.time()
    msg = await message.reply("ᴘᴏɴɢ!!!")
    end = time.time()
    telegram_ping = str(round((end - start) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))
    await msg.edit(f"""
𝗣𝗢𝗡𝗚 🥀!!
**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** {telegram_ping}
**sᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ:** {uptime}
        """)


custom_handler("ping",_ping)
