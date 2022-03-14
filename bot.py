from pyrogram import Client, filters

Bot=Client(
    "Bot",
    bot_token="5125014420:AAEK2E9aj-q9FHZknW_hrisJvCuONx0XPtU",
    api_id="17946666",
    api_hash="d9647913e97bf2f6a66d978290284028"
)

@Bot.on_message(filters.("start"))
async def start_message(bot, message):
    await message.reply_text("mission passed")


Bot.run()
