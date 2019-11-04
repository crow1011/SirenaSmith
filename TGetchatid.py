import telebot
import stngs

ip = '127.0.0.1'
port = '9050'

telebot.apihelper.proxy = {
  'https': 'socks5://{}:{}'.format(ip,port)
}
token = stngs.tgstngs()['token']
tb = telebot.TeleBot(token)

@tb.message_handler(commands=['start', 'help', 'chatid'])
def command_help(message):
    tb.reply_to(message, "Hello, your chat id: " + str(message.chat.id))

tb.polling()