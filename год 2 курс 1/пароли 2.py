class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(num):
    up = 0
    low = 0
    dig = 0
    abc = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    try:
        for elem in num:
            if elem.isdigit():
                dig += 1
            if elem.isupper():
                up += 1
            if elem.islower():
                low += 1
        if len(num) < 9:
            raise LengthError
        if low == 0 or up == 0:
            raise LetterError
        if dig == 0:
            raise DigitError
        for i in range(len(num) - 2):
            if any([num[i:i + 3].lower() in elem for elem in abc]):
                raise SequenceError
        return 'ok'
    except PasswordError as e:
        raise


try:
    print(check_password(" "))
except Exception as error:
    print(error.__class__.__name__)