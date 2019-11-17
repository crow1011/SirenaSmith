#!/usr/bin/python3
import sys
import checkclientconfig
import hashlib
import logging
import urllib3
import json

logging.basicConfig(filename="sirenaclient.log", level=logging.ERROR, format='%(asctime)s;%(levelname)s;%(message)s')
conf = checkclientconfig.getconf()
server_token=hashlib.md5(conf['server']['token'].encode('utf-8')).hexdigest()

encoded_body = json.dumps({
        "msg": sys.argv[1],
        "token": server_token,
        'alert':{'tg':conf['alert']['tg']}
    })

http = urllib3.PoolManager()

r = http.request('POST', conf['server']['host'],
                 headers={'Content-Type': 'application/json'},
                 body=encoded_body)
if r.status!='200':
	logging.error(r.status)



