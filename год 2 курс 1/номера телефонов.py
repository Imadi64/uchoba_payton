nomer_nekorrekt = input()
nomer = []
nomer_korrekten = []

for i in nomer_nekorrekt:
    nomer.append(i)

# if (nomer_nekorrekt[0] == '8'):
#     print('+7' + nomer_nekorrekt[1:-1])
#
# elif (nomer_nekorrekt[0] == '+' and nomer_nekorrekt[1] == '7'):
#     print('+7' + nomer_nekorrekt[2:-1])

print(nomer)
for i in range(len(nomer)):
    if (nomer[i] == '(') or (nomer[i] == ')') or \
            (nomer[i] == ' ') or (nomer[i] == '-'):
        del nomer[i]


# не удалть а добавлять числа в новый список
