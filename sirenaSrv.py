#!/usr/bin/python3
from flask import Flask, request, render_template
import logging
import sendTG, checkconfig
import hashlib


app = Flask(__name__)
app.config.from_object('config')
logging.basicConfig(filename="sirena.log", level=logging.ERROR, format='%(asctime)s;%(levelname)s;%(message)s')
conf=checkconfig.getconf()


@app.route('/', methods=['POST',])
def tg():
	if request.method=='POST':
		try:
			data = request.json
			if request.json['token']==hashlib.md5(conf['server']['token'].encode('utf-8')).hexdigest():
				if data['alert']['tg']=='True':
					sendTG.SendTG(request.json['msg'])
					return "ok"
			else:
				logging.error("Invalid sirena token in request data. Check sirena token config in sirena.conf and your sirena client config")
				return "read server log"
		except Exception as e:
			if 'token' not in request.json.keys():
				logging.error("No sirena token in request data. Check sirena token config in sirena.conf and your sirena client config")
			else:
				logging.error(e)
			return "read server log"


@app.route('/zabbix/', methods=['POST'])
def zabbix():
	try:
		data = request.json
		if request.json['token']==hashlib.md5(conf['server']['token'].encode('utf-8')).hexdigest():
			if data['alert']['tg']=='True':
				sendTG.SendTG(request.json['msg'])
				return "tg"
		else:
			logging.error("Invalid sirena token in request data. Check sirena token config in sirena.conf and your sirena client config")
			return "read server log"
	except Exception as e:
		if 'token' not in request.json.keys():
			logging.error("No sirena token in request data. Check sirena token config in sirena.conf and your sirena client config")
		else:
			logging.error(e)
		return "read server log"

@app.route('/status')
def status():
	return '''ok'''



if __name__ == '__main__':
    app.run(debug=True, host=conf['server']['ip'], port=conf['server']['port'])