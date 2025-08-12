from pyrogram import Client, filters
import os

# ---- Config ----
API_ID = 29822083
API_HASH = "7d2bfc0ad7766b23823cf779e7959e4b"
BOT_TOKEN = "8097625468:AAGFjME3Iqz0nakjwfkxPSxytWW3UOhTndU"

# ---- Create Bot Client ----
app = Client(
    "tnx_coin_farming",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ---- Start Command ----
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(
        "🚀 স্বাগতম **TNX COIN FARMING** বটে!\n\n"
        "🪙 এখানে আপনি মাইনিং শুরু করতে পারবেন।\n"
        "👉 `/mine` লিখে মাইনিং শুরু করুন।"
    )

# ---- Mine Command ----
@app.on_message(filters.command("mine"))
def mine(client, message):
    message.reply_text(
        "⛏ মাইনিং চলছে... 1 TNX আপনার অ্যাকাউন্টে যোগ হয়েছে ✅"
    )

# ---- Run Bot ----
print("✅ Bot is running...")
app.run()
