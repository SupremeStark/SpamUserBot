import os
import json 
from SpamUserBot import SUDO_USERS
from SpamUserBot.steve.funcs import custom_handler


async def sudo_list(client, message):
    try:
        await message.delete()
    except:
        pass
    text = "💝 sᴜᴅᴏ ᴜsᴇʀs:\n\n" 
    print(SUDO_USERS)
    for i in set(SUDO_USERS):
        user_id = int(i)
        try:
            mention = (await client.get_users(user_id)).mention
            text += f"• {mention}\n"
        except Exception as e:
            print(e)
    return await message.reply_text(text)


custom_handler("addsudo",_add_sudo)
custom_handler("rmsudo",_rm_sudo)
custom_handler("sudolist",sudo_list)




   



  
 
