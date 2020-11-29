nomera1 = set()
nomera2 = set()
a = input()
while a != "":
    nomera1.add(a)
    a = input()
b = input()
while b != "":
    nomera2.add(b)
    b = input()
od_nomera = nomera2 & nomera1
if len(od_nomera) == 0:
    print("EMPTY")
else:
    for i in od_nomera:
        print(i)