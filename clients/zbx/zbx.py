import json
import requests
import yaml
import os
import sys

sys.argv.append('alert')

BASEDIR = os.path.dirname(os.path.realpath(__file__))
SIRENA_PROBLEMS = []

def get_conf(config):
    path = BASEDIR+'/'+config
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data



def check_alive(servers):
    alives = []
    global SIRENA_PROBLEMS
    for server in servers:
        try:
            response = requests.get(server)
            if response.status_code==200:
                alives.append([server,response.elapsed.total_seconds()])
            else:
                SIRENA_PROBLEMS.append(server+'STATUS_CODE:'+response.status_code)
        except Exception as e:
            SIRENA_PROBLEMS.append(server+'PROBLEM: '+str(e))
            continue
    min = 666
    sort_alives = []
    for alive in alives:
        if alive[1]<min:
            min=alive[1]
            sort_alives.insert(0, alive)
        else:
            sort_alives.insert(-1, alive)
    return sort_alives



def send_msg(data, url):
    data_json = json.dumps(data)
    headers = {
        'Content-Type':'application/json',
    }
    response = requests.post(url=url, data=data_json, headers=headers)
    return response.status_code

def main():
    data = {'mesage':str(sys.argv[1])}
    data['sirena_problems'] = SIRENA_PROBLEMS
    conf = get_conf('zbx.yaml')
    alives = check_alive(conf['servers'])
    print(alives)
    for alive in alives:
        response_code = send_msg(data, alive[0])
        if response_code == 200:
            print(alive)
            break



if __name__=='__main__':
    main()