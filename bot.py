import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.environ.get("8245244001:AAH9wVmWe-K3i3mQd-ZvVXQgULC7luST6tA")
bot = telebot.TeleBot(TOKEN)

# ===== SETTINGS =====
CHANNEL_ID = -3575487358  # yaha apna channel ID dalna
INVITE_LINK = "https://t.me/+weJ7erS5u7BiNzRl"

FORCE_PHOTO = "AgACAgQAAxkBAAMCaY8xSVNX2BdUJlE84GMAAY_noVs6AALhC2sbPfN0UGeH_LzoBCQiAQADAgADeAADOgQ"
WELCOME_PHOTO = "AgACAgQAAxkBAAMEaY81VsbvguyK7cCdBTf87PPBlmEAAkO0MRsBZcVRHErApepJMRIBAAMCAAN4AAM6BA"
# =====================

def is_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

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

print("Bot Running...")
bot.infinity_polling()
