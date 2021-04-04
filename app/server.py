from aiohttp.web import Application, run_app
from aiohttp_json_rpc import JsonRpc

import yaml


def get_conf(conf_path: str) -> dict:
    with open(conf_path, 'r') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    return conf


conf = get_conf('conf/global.yml')
print(conf)


async def send(request):
    print(request.params)
    p = request.params
    print(p['mod'])
    print(get_conf(conf['mods']['send'][p['mod']]))
    return 'pong'


if __name__ == '__main__':
    rpc = JsonRpc()
    rpc.add_methods(
        ('', send),
    )

    app = Application()
    app.router.add_route('*', '/', rpc.handle_request)

    run_app(app, host='0.0.0.0', port=8080)
