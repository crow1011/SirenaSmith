import configparser
def getconf():
	parser = configparser.ConfigParser()
	parser.read_file(open('sirena.conf'))

	conf = {}
	for section in parser.sections():
		conf[section] = {}
		for key, val in parser.items(section):
			conf[section][key] = val
	return conf