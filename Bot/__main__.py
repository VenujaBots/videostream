from pyrogram import Client, idle
import os
from Bot.video_stream import app
API_ID = os.environ.get("API_ID",18862638)
API_HASH = os.environ.get("API_HASH","2a4a8dc0c1f6c9cb65f9f144439558ae")
TOKEN = os.environ.get("TOKEN","2143873439:AAF4v4I1m6y38KpkDFZpmSLKPHZW_0UKHa8")

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="Bot"),
)
bot.start()
app.start()
idle()
