import telebot
TOKEN = '1523598890:AAGLqPy9cLduQibAOFKyYJnbN0vlXzJ_-EA'
CHAT_ID = '356526705'

def send_message_to_bot(msg):
    bot = telebot.TeleBot(TOKEN)
    bot.config['api_key'] = TOKEN
    bot.send_message(CHAT_ID, msg)
