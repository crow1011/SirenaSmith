import os
import pytest
import sys
sys.path.append(os.getcwd())
from sirena import recipients
from sirena import sirena_config


def test_init():
    assert 2 + 2 == 4


def test_zabbix_create_case():
    msg = {'message': 'Top\nMiddle\nBottom\n',
           'type': 'new',
           'sirena_problems': [],
           'alerters': {'tg': {'enable': True},
                        'sirena_manager': {'enable': False}},
           'recipient': 'zabbix',
           'send_dt': 1493342530.669028}
    conf = sirena_config.get_conf()
    recipient = recipients.SirenaRecipient(msg, conf, 'zabbix')
    case = recipient.get_case()
    assert type(case) == dict
