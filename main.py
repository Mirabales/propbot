from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="📬 Hola Juan Pérez, tu renta mensual de RD$25,000 vence el día 5. — Tu asistente PropBot 🤖")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    app.run_polling()
