import telebot
from telebot import apihelper

def tg(message, send_to, api_key, proxy='None'):
    try:
        bot = telebot.TeleBot(api_key)
        apihelper.proxy = {'https': proxy}
        bot.send_message(send_to, message)
        return 'send'
    except Exception as e:
        return 'Error '+str(e)