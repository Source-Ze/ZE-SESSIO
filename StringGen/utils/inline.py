from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="» ⚡ ¦ بـدء إنـشـاء جـلسـة ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="جرۆبْ آلُدِعم", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="●○𝐙𝐄○●", url="https://t.me/UI_OS"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="🎙 بـايـࢪوجـࢪام 🎙", callback_data="pyrogram1"),
            InlineKeyboardButton(text="🎙 بـايـࢪوجـࢪام v2🎙", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="🎛 تـلـيـثـونـ 🎛", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
