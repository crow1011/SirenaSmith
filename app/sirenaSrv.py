from flask import Flask, request
import sirena_data, sirena_config, sirena_alerters

app = Flask(__name__, template_folder="templates")
conf = sirena_config.get_conf()



@app.route('/input/zabbix', methods=['POST','GET'])
def input_zabbix():
    if request.method=='GET':
        return 'ok'
    if request.method=='POST':
        status = sirena_data.analyzer(request.json,conf)
        return status




if __name__ == '__main__':
    app.run(debug=True,host=conf['server']['host'], port=conf['server']['port'])
