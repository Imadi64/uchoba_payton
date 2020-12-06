dom_bibl = []
sp_na_leto = []
a = int(input())
b = int(input())
for i in range(a):
    dom_bibl.append(input())
for i in range(b):
    sp_na_leto.append(input())
for kniga in sp_na_leto:
    if kniga in dom_bibl:
        print("YES")
    else:
        print("NO")