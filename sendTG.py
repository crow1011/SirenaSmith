import telebot
import stngs, checkconfig
conf = checkconfig.getconf()



def SendTG(msg):
	telebot.apihelper.proxy = {
	'https': 'socks5://{}:{}'.format(conf['proxy']['ip'],conf['proxy']['port'])
	}
	token = conf['tg']['bottoken']
	chatid = conf['tg']['chatid']
	tb = telebot.TeleBot(token)
	tb.send_message(chatid, msg)



