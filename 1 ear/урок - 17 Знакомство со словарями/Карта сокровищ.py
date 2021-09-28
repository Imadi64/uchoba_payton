chislo_koord = int(input())
spis = []
klad_max = 0
for a in range(chislo_koord):
    koordinati = input().split()
    spis.append(koordinati)

for i in spis:
    klad = 0
    for j in spis:
        if i[0][0: -1] == j[0][0: -1]:
            if i[1][0: -1] == j[1][0: -1]:
                klad += 1
    if klad > klad_max:
        klad_max = klad

print(klad_max)
