
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = os.getenv("BOT_TOKEN")
AUTHORIZED_USER_ID = os.getenv("AUTHORIZED_USER_ID")

def start(update: Update, context: CallbackContext):
    if str(update.effective_user.id) != str(AUTHORIZED_USER_ID):
        return
    update.message.reply_text("✅ ربات با موفقیت راه‌اندازی شد و فقط شما دسترسی دارید.")

if __name__ == "__main__":
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
