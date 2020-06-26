import telebot
from telebot import apihelper
from sirena import sirena_logger
logger=sirena_logger.get_logger()


def send_msg(message, send_to, api_key, proxy='None'):
    logger.debug('TG send message' + str(message))
    try:
        bot = telebot.TeleBot(api_key)
        if proxy!='None':
            apihelper.proxy = {'https': proxy}
        bot.send_message(send_to, message)
        return 'done'
    except Exception:
        logger.exception('TG Alerter: ')
        return 'error'

def check_connection():
    pass