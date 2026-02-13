import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import threading
from flask import Flask

# ================= CONFIG =================

TOKEN = os.environ.get("BOT_TOKEN")

CHANNEL_ID = -1003575487358  # ✅ Your Private Channel ID
INVITE_LINK = "https://t.me/+weJ7erS5u7BiNzRl"

FORCE_PHOTO = "AgACAgQAAxkBAAMCaY8xSVNX2BdUJlE84GMAAY_noVs6AALhC2sbPfN0UGeH_LzoBCQiAQADAgADeAADOgQ"
WELCOME_PHOTO = "AgACAgQAAxkBAAMEaY81VsbvguyK7cCdBTf87PPBlmEAAkO0MRsBZcVRHErApepJMRIBAAMCAAN4AAM6BA"

# ==========================================

bot = telebot.TeleBot(TOKEN)

# --------- FORCE JOIN CHECK ----------
def is_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

# --------- START COMMAND ----------
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"

    if not is_joined(user.id):
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton("PREMIUM VIDEO", url=INVITE_LINK)
        markup.add(btn)

        caption = f"""Hello {mention}

You need to join in my Channel/Group to use me

Kindly Please join Channel..."""

        bot.send_photo(
            message.chat.id,
            FORCE_PHOTO,
            caption=caption,
            parse_mode="HTML",
            reply_markup=markup
        )
    else:
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton("💎 BUY PREMIUM 💎", callback_data="buy")
        markup.add(btn)

        caption = f"""👋 Hello {mention}

🎖️ Want Premium?"""

        bot.send_photo(
            message.chat.id,
            WELCOME_PHOTO,
            caption=caption,
            parse_mode="HTML",
            reply_markup=markup
        )

# --------- BUTTON RESPONSE ----------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "buy":
        bot.send_message(call.message.chat.id, "💎 Premium Plans Coming Soon 🔥")

# --------- FAKE WEB SERVER FOR RENDER FREE PLAN ----------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()

print("Bot Running...")
bot.infinity_polling()
