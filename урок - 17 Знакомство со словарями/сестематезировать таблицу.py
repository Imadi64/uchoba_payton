chislo = int(input())
spisok_spiskov = [[]]
for i in range(chislo - 1):
    nabor_chisel = input()
    spisok_spiskov += [nabor_chisel.split()]
for i in range(chislo):
    stroka = ''
    for j in range(chislo):
        if i == j:
            stroka += '0 '
        elif j < i:
            stroka += spisok_spiskov[i][j] + ' '
        else:
            stroka += spisok_spiskov[j][i] + ' '
    print(stroka)
