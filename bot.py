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
          InlineKeyboardButton ("🌹JOIN GRUOP🌹", url="t.me/midnightmoviesofficial"),
          InlineKeyboardButton ("🌹JOIN CHANNEL🌹", url="t.me/FILE_ADD_CHANNEL"),
          ],[
          InlineKeyboardButton ("🌹BOT OWNER🌹", url="t.me/TEAM_NARUTO_GRUOP"),
          InlineKeyboardButton ("🌹BOT DEV🌹", url="t.me/PR0FESS0R_99"),
          ],[
          InlineKeyboardButton ("🌹BOT EDITING🌹", url="t.me/TEAM_NARUTO_GRUOP"),
          InlineKeyboardButton ("🌹REPO MAKE PART 1🌹", url="https://youtu.be/Af055Eozk9s"),
          ],[
          InlineKeyboardButton ("🌹SOURCE CODE🌹", url="https://github.com/SPIDEY-USER/IMDBFILTER"),
          Inlinekeyboardbutton ("🌹ADD ME TO A CHAT GRUOP🌹", url="http://t.me/{temp.U_NAME}?startgroup=true"),
          ]]
          )
       )
   

Bot.run()
