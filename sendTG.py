import telebot
import stngs

ip = '127.0.0.1'
port = '9050'

telebot.apihelper.proxy = {
  'https': 'socks5://{}:{}'.format(ip,port)
}
token = stngs.tgstngs()['token']
chatid = stngs.tgstngs()['chatid']
def SendTG(msg):
	tb = telebot.TeleBot(token)
	tb.send_message(chatid, msg)



