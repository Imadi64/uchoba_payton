s = input()
f = False
for symb in s:
    if symb == "_":
        if "a" <= symb <= "z":
            if "0" >= symb >= "9":
        print("OK")
        f = True
        break
if not f:
    print("Неверный символ:", symb )