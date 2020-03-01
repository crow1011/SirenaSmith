#!/usr/bin/python3
import sys
import checkclientconfig
import hashlib
import logging
import requests

logging.basicConfig(filename="srnzabbix.log", level=logging.ERROR, format='%(asctime)s;%(levelname)s;%(message)s')
conf = checkclientconfig.getconf()
conf['server']['host'] = conf['server']['host']+'zabbix/'
server_token=hashlib.md5(conf['server']['token'].encode('utf-8')).hexdigest()


response = requests.post(conf['server']['host'], json={
        "msg": sys.argv[1],
        "token": server_token,
        'alert':{'tg':conf['alert']['tg']}
    },headers={'Content-Type': 'application/json'} )



