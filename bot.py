import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 🔑 Environment variables
BOT_TOKEN = os.getenv("8657901169:AAEAib20IE7fpBic2p2743AftG4wJXFWFuk")
GEMINI_API_KEY = os.getenv("AIzaSyDU7i38rhCw_2hupBQj91DndTqR-SQJboM")

# Gemini setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# 🤖 Reply function
def get_reply(user_text):
    try:
        response = model.generate_content(user_text)
        return response.text
    except Exception as e:
        return "⚠️ Error, try again later"

# 📩 Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_text = update.message.text
    reply = get_reply(user_text)

    await update.message.reply_text(reply)

# 🚀 Run bot
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

print("Bot running on Railway...")
app.run_polling()
