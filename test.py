chislo = int(input())
minimym = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
spis = []
for i in range(chislo):
    spis.append(input())
for j in spis:
    if list(spis[j]) > list(spis[j + 1]):
        spis[j], spis[j + 1] = spis[j + 1], spis[j]
for i in spis:
    print(i)
