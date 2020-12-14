slovo = input()
min_slovo = "                                                      "
max_slovo = ""
n = 0
while slovo != "стоп":
    if len(slovo) < len(min_slovo):
        min_slovo = slovo
    if len(slovo) > len(max_slovo):
        max_slovo = slovo
    slovo = input()
for i in min_slovo:
    if i in max_slovo:
        n += 1
if n == len(min_slovo):
    print("ДА")
else:
    print("НЕТ")