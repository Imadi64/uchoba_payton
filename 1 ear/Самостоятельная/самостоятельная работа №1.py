prov_fraza = input()
prov_fraza = set(prov_fraza)
zanatia = input().split("; ")
spis = []
for i in zanatia:
    mno = set(i)
    n = 0
    for j in mno:
        if j in prov_fraza:
            n += 1
    if n > 7:
        spis.append(i)
print(" @ ".join(spis))
