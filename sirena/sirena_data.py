import sirena_alerters, sirena_logger
from datetime import datetime

logger = sirena_logger.get_logger()

def gen_msg(data,conf):
    message = data['message']+'\n'
    if conf['message']['problems']==True:
        if 'sirena_problems' in data.keys():
            for problem in data['sirena_problems']:
                message += '❌Problems: ' + problem + '\n'
    if conf['message']['try_datetime']==True:
        if 'try_dt' in data.keys():
            dt_format = conf['message']['datetime_format']
            message += '🟠Try: ' + datetime.fromtimestamp(data['try_dt']).strftime(dt_format) + '\n'
    if conf['message']['send_datetime']==True:
        if 'send_dt' in data.keys():
            dt_format = conf['message']['datetime_format']
            message += '🟢Send: ' + datetime.fromtimestamp(data['send_dt']).strftime(dt_format) + '\n'
    if conf['message']['sirena_name']==True:
        if 'sirena' in conf.keys():
            if 'name' in conf['sirena'].keys():
                message +='Sirena name: #' + conf['sirena']['name']
    return message

def sirena_manager_data(data,conf):
    pass

def tg_data(message, conf):
    send_id = conf['alerters']['tg']['default_send_id']
    api_key = conf['alerters']['tg']['api_key']
    if conf['alerters']['tg']['proxy']['enable']:
        proxy = conf['alerters']['tg']['proxy']['addr']
        res = sirena_alerters.tg(message, send_id, api_key, proxy)
    else:
        res = sirena_alerters.tg(message, send_id, api_key)
    if res == 'done':
        logger.info('sending alert from alerter TG: ' + str(message))
        return 'done'
    else:
        logger.error('ERROR sending from alerter TG: ' + str(res))
        return 'error'


def analyzer(data, conf):
    send_status = []
    if data['alerters']['tg']['enable']:
        message = gen_msg(data, conf)
        send_status.append(tg_data(message, conf))
    if data['alerters']['tg']['enable']:
        send_status.append(sirena_manager_data(data, conf))
    if 'error' not in send_status:
        return 'done'
    else:
        return 'error'