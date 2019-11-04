from flask import Flask, request
import logging
import sendTG, stngs
import hashlib

logging.basicConfig(filename="sirena.log", level=logging.ERROR, format='%(asctime)s;%(levelname)s;%(message)s')


app = Flask(__name__)


@app.route('/tg', methods=['POST'])
def tg():
	try:
		if request.json['token']==hashlib.md5(stngs.sirenaToken()['token'].encode('utf-8')).hexdigest():
			sendTG.SendTG(request.json['msg'])
			return "tg"
		else:
			logging.error("Invalid sirena token in request data. Check sirena token config in stngs.py and your sirena client config")
			return "read log"
	except:
		logging.error("No sirena token in request data. Check sirena token config in stngs.py and your sirena client config")
		return "read log"



if __name__ == '__main__':
    app.run(debug=True, host=stngs.hoststngs()['ip'])