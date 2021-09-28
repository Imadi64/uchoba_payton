VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def ask_password(login, password, success, failure):
    correct_vowels = True
    correct_consonants = True
    login, password = login.lower(), password.lower()
    if len(list(filter(lambda s: s in VOWELS, password))) != 3:
        correct_vowels = False
    if (list(filter(lambda s: s not in VOWELS, password)) !=
            list(filter(lambda s: s not in VOWELS, login))):
        correct_consonants = False
    if correct_vowels and correct_consonants:
        success(login)
    elif correct_vowels and not correct_consonants:
        failure(login, 'Wrong consonants')
    elif correct_consonants and not correct_vowels:
        failure(login, 'Wrong number of vowels')
    else:
        failure(login, 'Everything is wrong')


def main(login, password):
    def s(s):
        print(f'Привет, {s}!')

    def f(s, err):
        print(f'Кто-то пытался притвориться пользователем {s},'
              f' но в пароле допустил ошибку: {err.upper()}.')

    ask_password(login, password, s, f)


main("anastasia", "nsyatos")
main("eugene", "aanig")
ask_password("anastasia", "nsyatos", lambda login: print('super'), lambda login, err: print('bad'))