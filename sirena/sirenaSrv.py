from flask import Flask, request, jsonify
import sirena_data, sirena_config, sirena_alerters, sirena_logger

app = Flask(__name__)
conf = sirena_config.get_conf()
logger = sirena_logger.get_logger()


@app.route('/input/zabbix', methods=['POST', 'GET'])
def input_zabbix():
    if request.method == 'GET':
        return 'ok'
    if request.method == 'POST':
        status = sirena_data.analyzer(request.json, conf)
        return jsonify({'status': str(status)})


if __name__ == '__main__':
    app.run(debug=conf['server']['debug'], host=conf['server']['host'], port=conf['server']['port'])
