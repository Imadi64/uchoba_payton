password = 0
while password != "":
    password = input()
    new_password = input()
    if len(password) >= 8:
        if "123" not in password:
            if password == new_password:
                print("OK")
                break
            else:
                print("Различаются.")
        else:
            print("Простой!")
    else:
        print("Короткий!")
