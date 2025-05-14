from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id  # 🔥 Esto agarra el ID de quien escribe
    await context.bot.send_message(
        chat_id=user_id,
        text="📬 Hola, este es tu recordatorio de renta. — Tu asistente PropBot 🤖"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

