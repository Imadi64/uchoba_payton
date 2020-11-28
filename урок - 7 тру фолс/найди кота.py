n = int(input())
c = False
for i in range(n):
    a = input()
    if 'кот' in a or 'Кот' in a:
        c = True
if c == True:
    print('МЯУ')
else:
    print('НЕТ')
