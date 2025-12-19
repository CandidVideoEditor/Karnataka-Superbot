
from pyrogram import Client
from core.config import API_ID, API_HASH, BOT_TOKEN

def start_bot():
    app = Client("karnataka_superbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    print("Karnataka SuperBot running")
    app.run()
