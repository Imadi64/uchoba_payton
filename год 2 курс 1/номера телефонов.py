nomer_nekorrekt = input()
nomer = []
nomer_korrekten = []
sk1 = 0
sk2 = 0
sifri = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = 1

for i in nomer_nekorrekt:
    nomer.append(i)

if nomer[0] != '8':
    if nomer[0] != '+' and nomer[1] != '7':
        nomer_nekorrekt = 'error'

for i in nomer:
    if i == '(':
        sk1 += 1
    if i == ')':
        sk2 += 1

if sk1 != 1:
    if sk2 != 1:
        nomer_nekorrekt = 'error'

m = ''
for i in nomer:
    if (i == '-') and (m == '-'):
            nomer_nekorrekt = 'error'
            break
    m = i

for i in range(len(nomer)):
    if nomer[i] in sifri:
        nomer_korrekten.append(nomer[i])
for i in range(len(nomer_korrekten)):
    if 



if len(nomer_korrekten) != 11:
    nomer_nekorrekt == 'error'

if nomer_nekorrekt != 'error':
    print('+7' + ''.join(nomer_korrekten[1:]))

else:
    print('error')





# не удалть а добавлять числа в новый список
