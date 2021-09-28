chislo_odn = int(input())
napomin_d_r = {"янв": [], "фев": [], "мар": [], "апр": [], "май": [],
               "июн": [], "июл": [], "авг": [], "сен": [], "окт": [],
               "ноя": [], "дек": []}
for i in range(chislo_odn):
    odnokl = input().split(" ")
    mes = odnokl[2]
    napomin_d_r[mes].insert(0, odnokl[0])

vop_odn = int(input())
vop = []
for j in range(vop_odn):
    vop.append(input())

for i in vop:
    if i in napomin_d_r:
        if napomin_d_r[i] == []:
            print()
        else:
            print(" ".join(napomin_d_r[i]))
