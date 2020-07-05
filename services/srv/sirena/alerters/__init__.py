from sirena.alerters import tg
#if you need add alerter import alerter

class SirenaAlerter():
    def __init__(self, case, conf, alerter):
        self.case = case
        self.alerter = alerter
        self.conf = conf
        # if you need add alerter add element in alerters_list
        self.alerters_list = {
            'tg': tg
        }

    def send(self):
        sirena_alerter = self.alerters_list[self.alerter].Alert(self.case, self.conf)
        self.result = sirena_alerter.send_alert()
        return self.result