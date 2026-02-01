# © @ITSZSHUKLA
from telethon import events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# ---- ALL BOTS LIST ----
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# ---- START BUTTONS ----
START_BUTTON = [
    [Button.inline("𝗛𝗘𝗟𝗣 𝗔𝗡𝗗 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", data="help_back")],
    [
        Button.url("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", "https://t.me/Il_vip_support_lI"),
        Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", "https://t.me/+RVAhq8s84swzZWU1"),
    ],
    [
        Button.url("𝗩𝗜𝗣 ✘ 𝗔𝗗𝗜", "https://t.me/+RVAhq8s84swzZWU1"),
        Button.url("𝗥𝗘𝗣𝗢", "https://t.me/+RVAhq8s84swzZWU1"),
    ],
    [Button.url("𝗝𝗢𝗜𝗡 𝗙𝗢𝗥 𝗦𝗨𝗗𝗢", "https://t.me/+RVAhq8s84swzZWU1")],
]

# ---- REGISTER HANDLER FOR EACH BOT ----
def register_start(bot):
    @bot.on(events.NewMessage(pattern=r"^/start$"))
    async def start(event):
        if not event.is_private:
            return

        me = await event.client.get_me()

        text = (
            f"**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n"
            f"❍ 𝗛𝗘𝗬 ‣ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n"
            f"•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n"
            f"❍ 𝗜 𝗔𝗠 ‣ [{me.first_name}](tg://user?id={me.id})\n"
            f"•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n"
            f"● ɪ ᴀᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ ʙᴏᴛ ●\n"
            f"•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n"
            f"⊚ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ\n"
            f"⊚ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ\n"
            f"•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n"
            f"⦿ 24x7 ʀᴜɴ | "
            f"[𝗩𝗜𝗣 ✘ 𝗙𝗨𝗖𝗞𝗘𝗥](https://t.me/StrangerAssociation)\n"
            f"•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**"
        )

        await event.client.send_file(
            event.chat_id,
            file="https://i.ibb.co/JF8GP4zH/x.jpg",
            caption=text,
            buttons=START_BUTTON,
        )

# ---- APPLY TO ALL BOTS ----
for bot in BOTS:
    register_start(bot)
