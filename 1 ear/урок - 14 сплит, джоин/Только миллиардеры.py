kol_deneg = input().split(';')
for i in range(len(kol_deneg)):
    kol_deneg_2 = kol_deneg[i].split(',')
    elementi = []
    for j in kol_deneg_2:
        if int(j) > 999999999:
            elementi.append(j)
    print(','.join(elementi))
