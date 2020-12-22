chislo_odn = int(input())
napomin_d_r = dict()
for i in range(chislo_odn):
    odnokl = input().split(" ")
    mes = odnokl[0]
    napomin_d_r[mes] = odnokl[-1]
vop_odn = int(input())
vop = []
for j in range(vop_odn):
    vop.append(input())
for i in vop:
    for key, value in napomin_d_r.items():
        if value == i:
            print(key, end=" ")
    print()