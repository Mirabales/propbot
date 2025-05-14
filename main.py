
import os
import datetime
import telegram

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

rent_due_day = 5
today = datetime.datetime.now()
current_day = today.day

# Calculate days until due
if current_day > rent_due_day:
    if today.month == 12:
        due_date = datetime.datetime(today.year + 1, 1, rent_due_day)
    else:
        due_date = datetime.datetime(today.year, today.month + 1, rent_due_day)
else:
    due_date = datetime.datetime(today.year, today.month, rent_due_day)

days_until_due = (due_date - today).days

message = f"""📬 Hola Juan Pérez,

Recordatorio amistoso: tu renta mensual de RD$25,000 vence el día {rent_due_day}.
Faltan {days_until_due} días.

Gracias por tu puntualidad y por mantener buena comunicación.

— Tu asistente PropBot 🤖"""

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text=message)
