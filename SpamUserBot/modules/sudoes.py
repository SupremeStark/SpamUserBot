import os
import json 
from SpamUserBot import SUDO_USERS
from SpamUserBot.steve.funcs import custom_handler,extract_user_id

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "SpamUserBot/sudo.json")

async def _add_sudo(client, message):
    user_id = await extract_user_id(message)
    try:
        await message.delete()
    except:
        pass    
    if not user_id:
        return await message.reply("ʙʀᴜʜ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ.")
    if user_id in SUDO_USERS:
        return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ sᴜᴅᴏ ᴜsᴇʀ.")
  #  with open(ELEVATED_USERS_FILE, "r") as infile:
  #       data = json.load(infile)
   # data["sudos"].append(user_id)
    SUDO_USERS.append(user_id)
   # with open(ELEVATED_USERS_FILE, "w") as outfile:
  #      json.dump(data, outfile, indent=4)
    return await message.reply_text("ᴀᴅᴅᴇᴅ ᴛʜɪs ᴜsᴇʀ ɪɴ sᴜᴅᴏ ᴜsᴇʀs.")

async def _rm_sudo(client, message):
    user_id = await extract_user_id(message)
    try:
        await message.delete()
    except:
        pass   
    if not user_id:
        return await message.reply("ʙʀᴜʜ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ.")
    
    if user_id not in SUDO_USERS:
        return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴀɪɴ'ᴛ ᴀ sᴜᴅᴏ ᴜsᴇʀ ᴀɴʏᴡᴀʏ ɪɢɴᴏʀᴇ ʜɪᴍ.")
    SUDO_USERS.remove(user_id)    
    return await message.reply_text("ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs")

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




   



  
 
