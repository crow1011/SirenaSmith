import telebot
import checkconfig

conf = checkconfig.getconf()
token = conf['tg']['bottoken']
tb = telebot.TeleBot(token)
if conf['proxy']['proxy']=='True':
	telebot.apihelper.proxy = {
  		'https': 'socks5://{}:{}'.format(conf['proxy']['ip'],conf['proxy']['port'])
	}

@tb.message_handler(commands=['start', 'help', 'chatid'])
def command_help(message):
    tb.reply_to(message, "Hello, your chat id: " + str(message.chat.id))

tb.polling()