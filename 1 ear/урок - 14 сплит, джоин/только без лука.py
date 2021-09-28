kol = int(input())
s = []
m = []
for j in range(kol):
    predl = input()
    s.append(predl)
for i in s:
    if "лук" in i:
        a = 1
    else:
        m.append(i)
print(", ".join(m))
