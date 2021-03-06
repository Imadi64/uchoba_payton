from sys import exit


class MailClient:
    def __init__(self, server, user):
        self.s = server
        self.u = user

    d = dict()

    def f(self):
        return self.d

    def list(self):
        self.d[self.s] = self.u


class Receive(MailClient):

    def __init__(self):
        super().f()

    def Mail(self):
        s = input('На какой сервер зайти? ')
        if s in self.d.keys():
            if type(self.d[s]) == tuple:
                print(
                    f'Получено письмо от пользователя'
                    f'{self.d[s][0]}: {self.d[s][1]}')
            else:
                print('В папке "Вся почта" пусто')
        else:
            print('ERROR!!! Что-то пошло не так ¯\_(ツ)_/¯')


class Send(MailClient):

    def __init__(self):
        super().f()

    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k

    def send(self):
        un = input('Кому написать письмо? ')
        if un in self.d.values() and len(self.d[self.get_key(self.d, un)]) > 1:
            tom = input('Введи текст сообщения: ')
            for i in self.d.values():
                if i == un:
                    self.d[self.get_key(self.d, un)] = (i, tom)
            print(f'Сообщение успешно отправлено {un}!')
        else:
            print('ERROR!!! пользователь необнанужен'
                  'наверное его нет в базе данных ¯\_(ツ)_/¯')


def main():
    while True:
        print('Привет! Вы попали на почтовый сервис AmEl!')
        serv = input('На какой сервер зайти? ')
        name = input('Как мне вас называть? ')
        print(f'{name[0].upper() + name[1:].lower()}, добро пожаловать!')
        m = MailClient(serv, name)
        m.list()
        way = input('Что надо сделать? ')
        if way.lower().strip() == 'отправить сообщение'\
                or way.lower().strip() \
                == 'написать сообщение' or way.lower().strip() == 'написать':
            s = Send()
            s.send()
        elif way.lower().strip() == 'просмотреть ящик'\
                or way.lower().strip() == 'посмотреть сообщения' \
                or way.lower().strip() == 'прочитать сообщения'\
                or way.lower().strip() == 'почитать' \
                or way.lower().strip() == 'посмотреть почту':
            r = Receive()
            r.Mail()
        else:
            print('ERROR!!! неправильная команда')

        print('/-----------------------------------------\ ')
        s = '|"exit" - выйти'
        s2 = '"return" - вернуться на домашнюю страницу|'
        print(s, s2, sep="\n")
        print('\-----------------------------------------/ ')
        a = input()
        if a == 'exit':
            exit()
        elif a == 'return':
            pass
        else:
            print('ERROR!!! неправильная команда')
            print('Надо: 1. exit - выход')
            print('      2. return - вернуться на домашнюю страницу')
            exit()


main()
