
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ James Gold Auto Bot চালু আছে! 🤖\n\n"
        "Telegram signal এলে এখানে প্রসেস করা হবে."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot commands:\n"
        "/start - Bot চালু আছে কিনা দেখুন\n"
        "/help - Help"
    )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        print("ERROR: BOT_TOKEN is not set")
        return

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
