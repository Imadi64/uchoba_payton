orel_reshka = input()
n = 0
a = 0
for i in orel_reshka:           # рооррооор
    if i == "о":
        n += 1
    else:
        n = 0
    if a < n:
        a = n
print(a)