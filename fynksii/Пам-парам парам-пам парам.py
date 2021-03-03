a = input()
glasnie = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю", "ё"]
b = a.split(" ")
kol_glasn_bykv = []
n = 0
for i in b:
    n = 0
    if n != 0:
        kol_glasn_bykv.append(n)
    for j in i:
        if j in glasnie:
            n += 1

if all(x == kol_glasn_bykv[0] for x in kol_glasn_bykv) == True:
    print("Парам пам-пам")
else:
    print("Пам парам")
