f_eng = set()
f_nem = set()
kol_eng = int(input())
kol_nem = int(input())
for i in range(kol_eng):
    f_eng.add(input())

for i in range(kol_nem):
    f_nem.add(input())

f = f_eng ^ f_nem
if len(f) == 0:
    print("NO")
else:
    print(len(f))