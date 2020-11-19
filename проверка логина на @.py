login = input()
el_pochta = input()
if "@" in login:
    print("Некорректный логин")
elif "@" not in el_pochta:
    print("Некорректный адрес")
else:
    print("OK")
