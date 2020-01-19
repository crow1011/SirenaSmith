import telebot, logging
import checkconfig
conf = checkconfig.getconf()
logging.basicConfig(filename="sirena.log", level=logging.ERROR, format='%(asctime)s;%(levelname)s;%(message)s')



def SendTG(msg):
	try:
		if conf['proxy']['proxy']=='True':
			telebot.apihelper.proxy = {
			'https': 'socks5://{}:{}'.format(conf['proxy']['ip'],conf['proxy']['port'])
			}
		token = conf['tg']['bottoken']
		chatid = conf['tg']['chatid']
		tb = telebot.TeleBot(token)
		tb.send_message(chatid, msg)
	except Exception as er:
		if (er==ConnectionError)and(conf['proxy']['proxy']=='True'):
			logging.error("proxy ConnectionError, check sirena.conf")
		else:
			logging.error(er)



