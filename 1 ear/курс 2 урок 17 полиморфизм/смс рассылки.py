class Person:
    def __init__(self, name, otch, surn, x):
        self.name = name
        self.otch = otch
        self.surn = surn
        self.x = x

    def get_phone(self):
        if 'private' in self.x:
            return self.x['private']
        else:
            return

    def get_name(self):
        return f'{self.surn} {self.name} {self.otch}'

    def get_work_phone(self):
        if 'work' in self.x:
            return self.x['work']
        else:
            return

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.otch}! Примите участие в нашем' \
               f' беспроигрышном конкурсе для физических лиц'
