import telebot
from telebot import apihelper
from datetime import datetime
from sirena import sirena_logger

logger = sirena_logger.get_logger()


class Alert():
    def __init__(self, case, conf):
        self.case = case
        self.conf = conf
        self.send_to = self.conf['alerters']['tg']['default_send_id']
        self.status = self.conf['alerters']['tg']['enable']
        self.bot = telebot.TeleBot(self.conf['alerters']['tg']['api_key'])

    def gen_msg(self, message):
        if self.conf['message']['problems']:
            if 'problems' in self.case.keys():
                message += '❌Problems: ' + self.case['problems'] + '\n'
        if self.conf['message']['try_datetime']:
            if 'try' in self.case.keys():
                dt_format = self.conf['message']['datetime_format']
                message += '🟠Try: ' + datetime.fromtimestamp(self.case['try']).strftime(dt_format) + '\n'
        if self.conf['message']['send_datetime']:
            if 'send' in self.case.keys():
                dt_format = self.conf['message']['datetime_format']
                message += '🟢Send: ' + datetime.fromtimestamp(self.case['send']).strftime(dt_format) + '\n'
        if self.conf['message']['sirena_name']:
            if 'sirena' in self.conf.keys():
                if 'name' in self.conf['sirena'].keys():
                    message += 'Sirena name: #' + self.conf['sirena']['name']
        return message

    def send_alert(self):
        # generate message
        self.message = self.gen_msg(self.case['message'] + '\n')
        # check alerter status
        if self.status:
            logger.debug('TG send message' + str(self.message))
            if self.conf['alerters']['tg']['proxy']['enable']:
                apihelper.proxy = {'https': self.conf['alerters']['tg']['proxy']['addr']}
            if self.case['output']['tg'] != '':
                self.bot.send_message(self.case['output']['tg']['send_to'], self.message)
            else:
                self.bot.send_message(self.send_to, self.message)
            return 'done'
