# main.py
import os
from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

app = Flask(__name__)

# Telegram bot tokenini o'rnating
TOKEN = os.environ.get('BOT_TOKEN', '7249800610:AAF8lq68BsFVm-6leMV-FCegwMq-eqg6_cM')
bot = telegram.Bot(token=TOKEN)

# Webhook URL uchun
url = os.environ.get('URL', 'YOUR_RAILWAY_URL')

# Bot komandalarini boshqarish
def start(update, context):
    update.message.reply_text('Salom! Men webhook orqali ishlayotgan botman.')

def echo(update, context):
    update.message.reply_text(update.message.text)

# Webhook uchun Flask route
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(), bot)
    
    # Xabarni qayta ishlash
    if update.message is not None:
        if update.message.text.startswith('/start'):
            update.message.reply_text('Salom! Men webhook orqali ishlayotgan botman.')
        else:
            update.message.reply_text(update.message.text)
    
    return 'ok'

# Webhook o'rnatish
@app.route('/set_webhook')
def set_webhook():
    s = bot.set_webhook(f'{url}/webhook')
    if s:
        return 'Webhook muvaffaqiyatli o\'rnatildi!'
    return 'Webhook o\'rnatishda xatolik yuz berdi'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)