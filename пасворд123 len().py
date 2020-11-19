password = input()
new_password = input()
if len(password) >= 8:
    if password == new_password:
        print("OK")
    else:
        print("Различаются.")
else:
    print("Короткий!")
