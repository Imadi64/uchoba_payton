def who_are_you_and_hello():
    name = input()
    while not (name.isalpha() and name[0].isupper() and name[1:].islower()):
        name = input()
    print("Привет,", name + "!")


who_are_you_and_hello()
