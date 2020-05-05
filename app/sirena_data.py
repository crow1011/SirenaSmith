import sirena_alerters, sirena_logger
logger = sirena_logger.get_logger()

def analyzer(data, conf):
    if data['alerters']['tg']['enable']:
        message = data['message']
        send_id = conf['alerters']['tg']['default_send_id']
        api_key = conf['alerters']['tg']['api_key']
        if conf['alerters']['tg']['proxy']['enable']:
            proxy = conf['alerters']['tg']['proxy']['addr']
            res = sirena_alerters.tg(message, send_id, api_key, proxy)
        else:
            res = sirena_alerters.tg(message, send_id, api_key)
        if res=='done':
            logger.info('sending alert from alerter TG: '+str(message))
            return 'done'
        else:
            logger.error('ERROR sending from alerter TG: ' + str(res))
            return 'error'
