"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @reeshu_xd
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "GodHackerz User"
PM_IMG = "https://telegra.ph/file/8e929112328df851306e4.jpg"
pm_caption = "**This is GodHackerz Userbot**\n\n"

pm_caption += "Hi THERE 👋 MASTER ! I am Alive. All functions are working properly.\n\n"
pm_caption += "⚡️Status⚡️\n\n"
pm_caption += "😎Telethon Version : (1.16.04)\n"
pm_caption += "🥳Python : (3.8.3)\n"
pm_caption += "😮Version : (1.0)\n"
pm_caption += "🥱A.I Verision : Beta **1.0.01** [Ask Support Group](t.me/Godhackerzuserbot)\n"
pm_caption += "😱Sudo : (enabled For Master)\n"
pm_caption += "🤫Database status : All Fine👌\n"
pm_caption += f"🥰My Pro Master : {DEFAULTUSER}\n\n"
pm_caption += "🤖[✅ Deploy Me Now ✅](https://github.com/rohithaditya/Godhackerz-userbot.git)\n\n"
pm_caption += "© [GodHackerz Userbot](https://github.com/rohithaditya/Godhackerz-userbot/blob/main/LICENSE)\n\n"
pm_caption += "    [GODHACKERZ](https://t.me/Godhackerzuserbot) For Latest Updates\n\n"
pm_caption += "SYSTEM HEALTH : STABLE 😎👍 "
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
