def ask_password():
    parol = "password"
    popitki = 0
    while popitki != 3:
        parol1 = input()

        if parol1 == parol:
            print("Пароль принят")
            break

        popitki += 1
    if popitki == 3:
        print("В доступе отказано")


ask_password()
