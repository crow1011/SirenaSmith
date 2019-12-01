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
	parser.read_file(open('sirenaclient.conf'))

	conf = {}
	for section in parser.sections():
		conf[section] = {}
		for key, val in parser.items(section):
			conf[section][key] = val
	if check(conf['server']['host1']):
		conf['server']['host']=conf['server']['host1']
	if check(conf['server']['host2']):
		conf['server']['host']=conf['server']['host2']
	if check(conf['server']['host3']):
		conf['server']['host']=conf['server']['host3']
	return conf