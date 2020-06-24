import telebot
from telebot import apihelper
from sirena import sirena_config

conf = sirena_config.get_conf()
if conf['alerters']['tg']['proxy']['enable']:
    proxy = conf['alerters']['tg']['proxy']['addr']

api_key = conf['alerters']['tg']['api_key']
bot = telebot.TeleBot(api_key)
apihelper.proxy = {'https': proxy}

@bot.message_handler(commands=['get_chat_id'])
def get_id(message):
    bot.send_message(message.chat.id, str(message.chat.id))

if __name__=='__main__':
    bot.polling()