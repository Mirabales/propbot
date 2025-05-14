from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ✅ Datos de prueba para este ejemplo:
TENANT_NAME = "Juan Pérez"
RENT_AMOUNT = 25000  # en pesos dominicanos
DUE_DAY = 5

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    message = (
        f"📬 Hola {TENANT_NAME},\n\n"
        f"Este es un recordatorio de tu renta mensual:\n"
        f"💰 Monto: RD${RENT_AMOUNT:,}\n"
        f"📅 Fecha de vencimiento: día {DUE_DAY} de cada mes\n\n"
        f"Gracias por tu puntualidad 🙏🏼\n"
        f"— Tu asistente PropBot 🤖"
    )
    await context.bot.send_message(chat_id=user_id, text=message)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

