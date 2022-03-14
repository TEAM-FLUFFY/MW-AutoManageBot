from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot=Client(
    "Imdb Bot",
    bot_token="5125014420:AAEK2E9aj-q9FHZknW_hrisJvCuONx0XPtU",
    api_id="17946666",
    api_hash="d9647913e97bf2f6a66d978290284028"
)

@Bot.on_message(filters.command("start"))
async def start_message(bot, message):
   await message.reply_text(
       text="**ഈ ചാനലിലും ഗ്രുഒപ്പിലും നിങ്ങൾ ഇല്ല ഇത്രെയും വേഗം ജോയിൻ ആവേണ്ടതാണ്🔥🔥**",
       reply_markup=InlineKeyboardMarkup( [[
          Inlinekeyboardbutton ("🌹ADD ME TO A CHAT GRUOP🌹", url="http://t.me/{temp.U_NAME}?startgroup=true")
          ]]
          )
       )
   

Bot.run()
