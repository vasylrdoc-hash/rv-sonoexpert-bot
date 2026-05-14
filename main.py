from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = "ТУТ_ТВІЙ_TOKEN"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Отримано: {text}")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
