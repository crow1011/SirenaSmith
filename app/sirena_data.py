import sirena_alerters, sirena_logger

logger = sirena_logger.get_logger()

def gen_msg(data,conf):
    message = data['message']+'\n'
    if conf['message']['problems']==True:
        if 'sirena_problems' in data.leys():
            for problem in data['sirena_problems']:
                message += problem + '\n'
    if conf['message']['try_datetime']==True:
        if 'try_dt' in data.keys():
            message +=

def sirena_manager_data(data,conf):
    pass
def tg_data(data, conf):
    message = data['message']
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
        send_status.append(tg_data(data, conf))
    if data['alerters']['tg']['enable']:
        send_status.append(sirena_manager_data(data, conf))
    if 'error' not in send_status:
        return 'done'