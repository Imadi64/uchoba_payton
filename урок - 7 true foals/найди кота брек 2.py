flag = False
string = input()
cout = 1
number = 0
while string != 'СТОП':
    if 'Кот' in string or 'кот' in string:
        flag = True
        number = cout
        break
    else:
        flag = False
    cout = cout + 1
    string = input()
if flag:
    print(number)
else:
    print(-1)