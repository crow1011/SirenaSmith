import configparser
import requests

def check(url):
    try:
        requests.get(url+'status', timeout=1)
        return True
    except: 
        return False

def getconf():
	parser = configparser.ConfigParser()
	parser.read_file(open('srnzabbix.conf'))

	conf = {}
	for section in parser.sections():
		conf[section] = {}
		for key, val in parser.items(section):
			conf[section][key] = val
	conn = False
	srvs = conf['server']['hosts'].split(',')
	for srv in srvs:
		if check(srv):
			conf['server']['host']=srv
	return conf
