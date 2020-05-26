#! /usr/bin/env python3
import json
import requests
import yaml
import os
import sys
import logging
from datetime import datetime

sys.argv.append('no message')

BASEDIR = os.path.dirname(os.path.realpath(__file__))
SIRENA_PROBLEMS = []


def get_logger(conf):
    log_file = BASEDIR + '/' + conf['logger']['log_path']
    logger = logging.getLogger(__name__)
    # set logging level
    if conf['logger']['level'] == 'debug':
        level = logging.DEBUG
    if conf['logger']['level'] == 'info':
        level = logging.INFO
    if conf['logger']['level'] == 'warning':
        level = logging.WARNING
    if conf['logger']['level'] == 'ERROR':
        level = logging.ERROR
    logger.setLevel(level)
    # create the logging file handler
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger



def get_conf(config):
    path = BASEDIR + '/' + config
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


conf = get_conf('zbx.yaml')
logger = get_logger(conf)


def check_alive(servers):
    alives = []
    global SIRENA_PROBLEMS
    for server in servers:
        try:
            response = requests.get(server)
            if response.status_code == 200:
                alives.append([server, response.elapsed.total_seconds()])
            else:
                SIRENA_PROBLEMS.append(server + 'STATUS_CODE:' + response.status_code)
        except Exception as e:
            SIRENA_PROBLEMS.append(server + ' PROBLEM: ' + str(e))
            continue
    min = 666
    sort_alives = []
    for alive in alives:
        if alive[1] < min:
            min = alive[1]
            sort_alives.insert(0, alive)
        else:
            sort_alives.insert(-1, alive)
    return sort_alives


def send_msg(data, url):
    data['send_dt'] = datetime.today().timestamp()
    data_json = json.dumps(data)
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url=url, data=data_json, headers=headers)
    return response.json()['status']


def check_heap(conf):
    heap_path = BASEDIR + '/' + conf['heap']['heap_file']
    with open(heap_path, 'r') as f:
        heap = f.read().split('\n')
        if len(heap) != 0:
            return True
        else:
            return False


def add_heap(data, conf):
    data['try_dt'] = datetime.today().timestamp()
    heap_path = BASEDIR + '/' + conf['heap']['heap_file']
    with open(heap_path, 'a+') as f:
        j_data = json.dumps(data)
        f.write(j_data + '\n')
        f.close()
    return True


def clean_heap(conf, url):
    heap_path = BASEDIR + '/' + conf['heap']['heap_file']
    with open(heap_path, 'r') as f:
        data = f.read().split('\n')
        for dat in data:
                if dat!='':
                    j_dat = json.loads(dat)
                    send_msg(j_dat, url)
    f.close()
    open(heap_path, 'w')
    if not check_heap(conf):
        return True
    else:
        return False


def main():
    data = {'message': str(sys.argv[1])}
    data['type'] = 'new'
    data['sirena_problems'] = SIRENA_PROBLEMS
    data['alerters'] = conf['alerters']
    alives = check_alive(conf['servers'])
    not_send = True
    for alive in alives:
        response_status = send_msg(data, alive[0])
        if response_status == 'done':
            not_send = False
            if check_heap(conf):
                clean_heap(conf,alive[0])
            break

    if not_send:
        add_heap(data, conf)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        logger.exception('#Exceprion ')
