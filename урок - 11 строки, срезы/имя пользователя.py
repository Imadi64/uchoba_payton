hars = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
nik_name = list(input())
for i in nik_name:
    if i not in '1234567890_qwertyuiopasdfghjklzxcvbnm':
        print('Неверный символ:', i)
        break
else:
    print('OK')