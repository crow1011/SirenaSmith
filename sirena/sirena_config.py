import yaml

def get_conf():
    with open('/etc/sirena/sirena.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data