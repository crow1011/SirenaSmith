from sirena.recipients import zabbix

class SirenaRecipient():
    def __init__(self, msg, conf, recipient):
        self.msg = msg
        self.recipient = recipient
        self.conf = conf
        self.recipients_list = {
            'zabbix': zabbix
        }

    def get_case(self):
        sirena_recipient = self.recipients_list[self.recipient].Case(self.msg, self.conf)
        self.case = sirena_recipient.case_gen()
        return self.case
