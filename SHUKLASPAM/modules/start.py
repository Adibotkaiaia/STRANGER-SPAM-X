# © @ITSZSHUKLA
from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("𝗛𝗘𝗟𝗣 𝗔𝗡𝗗 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", data="help_back")
    ],
    [
        Button.url("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", "https://t.me/Il_vip_support_lI"),
        Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", "https://t.me/+RVAhq8s84swzZWU1")
    ],
    [
        Button.url("VIP_ADI", "https://t.me/+RVAhq8s84swzZWU1"),
        Button.url("𝗥𝗘𝗣𝗢", "https://t.me/+RVAhq8s84swzZWU1")
    ],
    [
        Button.url("𝗝𝗢𝗜𝗡 𝗙𝗢𝗥 𝗦𝗨𝗗𝗢", "https://t.me/+RVAhq8s84swzZWU1")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        ShuklaBot = await event.client.get_me()
        bot_name = ShuklaBot.first_name
        bot_id = ShuklaBot.id
        TEXT = f"**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗛𝗘𝗬 ‣ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗜 𝗔𝗠 ‣ [{bot_name}](tg://user?id={bot_id})\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n● ɪ ᴀᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ ʙᴏᴛ ●\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ \n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⦿ 24x7 ʀᴜɴ|[sᴛʀᴀɴɢᴇʀ](https://t.me/StrangerAssociation)\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**"
        await event.client.send_file(
            event.chat_id,
            "https://i.ibb.co/JF8GP4zH/x.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
