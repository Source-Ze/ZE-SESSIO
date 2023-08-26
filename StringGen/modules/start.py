from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"""📟¦اهلا بـك عزيـزي 📬 {msg.from_user.mention},
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة

بواسطـة : [زيـــــــٌن اݪــتأࢪيخ 🚸](tg://user?id=6300938349) !""",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
