import sirena_alerters

def analyzer(data,conf):
    if data['alerters']['tg']['enable']:
        message = data['message']
        send_id = conf['alerters']['tg']['default_send_id']
        api_key = conf['alerters']['tg']['api_key']
        if conf['alerters']['tg']['proxy']['enable']:
            proxy = conf['alerters']['tg']['proxy']['addr']
            res = sirena_alerters.tg(message, send_id, api_key, proxy)
        else:
            res = sirena_alerters.tg(message, send_id, api_key)
        print(res)
    return 'done'