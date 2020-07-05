from flask import Flask, request, jsonify
from sirena import sirena_data, sirena_config, sirena_alerters, sirena_logger, recipients, alerters

app = Flask(__name__)
conf = sirena_config.get_conf()
logger = sirena_logger.get_logger()


@app.route('/input/zabbix', methods=['POST', 'GET'])
def input_zabbix():
    if request.method == 'GET':
        return 'ok'
    if request.method == 'POST':
        recipient = recipients.SirenaRecipient(request.json, conf, 'zabbix')
        case = recipient.get_case()
        status = {}
        for alerter_name in case['output']:
            alerter = alerters.SirenaAlerter(case, conf, alerter_name)
            if alerter.send()=='done':
                status[alerter_name] = True
            else:
                status[alerter_name] = False
        return jsonify(status)


if __name__ == '__main__':
    app.run(host=conf['server']['host'], port=conf['server']['port'])
