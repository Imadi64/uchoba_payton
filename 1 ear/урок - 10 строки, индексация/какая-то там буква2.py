s = input('Введите сообщение: ')
n = int(input('Введите натуральное число: '))
if (0 < n <= len(s)):
    print(s[n - 1])
else:
    print('ОШИБКА')
