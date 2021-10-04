nomer_nekorrekt = input()
nomer = []
nomer_korrekten = []
sk1 = 0
sk2 = 0
sifri = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = 1

for i in nomer_nekorrekt:
    nomer.append(i)

if nomer_nekorrekt[0] != '8':
    if nomer_nekorrekt[0] == '+' and nomer_nekorrekt[1] == '7':
        nomer_nekorrekt = 'error'

for i in nomer:
    if i == '(':
        sk1 += 1
    if i == ')':
        sk2 += 1

if sk1 + sk2 != 2:
    if sk1 + sk2 != 0:
        nomer_nekorrekt = 'error'

for i in range(len(nomer)):
    if nomer[i] != nomer[-1]:
        if nomer[i] == '-' and nomer[i + 1] == '-':
            nomer_nekorrekt = 'error'

for i in range(len(nomer)):
    if nomer_nekorrekt == 'error':
        break
    else:
        if nomer[i] in sifri:
            nomer_korrekten.append(nomer[i])

for i in nomer_korrekten:
    if nomer_nekorrekt == 'error':
        print('error')
        break
    else:

        if (len(nomer) == 11) and (a != 0):
            print('+7', end='')
            a = 0
        else:
            print(i, end='')





# не удалть а добавлять числа в новый список
