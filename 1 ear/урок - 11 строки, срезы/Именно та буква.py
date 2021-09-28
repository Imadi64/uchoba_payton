s = input()
n = int(input())
predlojenie = input()
if (0 < n <= len(s)) and predlojenie == s[n - 1] and len(predlojenie) == 1:
    print('ДА')
elif (0 < n <= len(s)) and predlojenie != s[n - 1] and len(predlojenie) == 1:
    print('НЕТ')
else:
    print('ОШИБКА')
