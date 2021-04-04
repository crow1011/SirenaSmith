import requests


def http(request) -> str:
    print(request.params)
    return 'http OK'
