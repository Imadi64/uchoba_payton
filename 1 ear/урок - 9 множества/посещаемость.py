sp_urokov = []
kol_urokov = int(input())
for i in range(kol_urokov):
    kol_uchenikov = int(input())
    for j in range(kol_uchenikov):
        sp_urokov.append(input())

molochi = set()
for i in sp_urokov:
    if sp_urokov.count(i) == kol_urokov:
        molochi.add(i)

for i in molochi:
    print(i)
