class Case():
    def __init__(self, msg, conf):
        self.case = {}
        self.msg = msg
        self.conf = conf

    def validation(self):
        return True

    def case_gen(self):
        # create case with alerters
        if self.validation():
            self.case['input'] = self.msg['recipient']
            self.case['message'] = self.msg['message']
            self.case['output'] = []
            # gen enable alerters list
            for alerter in self.msg['alerters']:
                if self.msg['alerters'][alerter]['enable']:
                    self.case['output'].append(alerter)
            #convert problems array to string
            self.case['problems'] = ''
            for problem in self.msg['sirena_problems']:
                self.case['problems'] += str(problem)
            self.case['send'] = self.msg['send_dt']
            #if alert now send first try client set timestamp
            if 'try_dt' in self.msg.keys():
                self.case['try'] = self.msg['try_dt']
            return self.case