ima_pol = ''


def polite_input(question):
    global ima_pol
    if question == "Как вас зовут":
        print('Как вас зовут?')
        ima_pol = input()
        return ima_pol
    elif question == "укажите возраст":
        print(f"{ima_pol}, укажите возраст")
        age = input()
        return age
    elif question == 'укажите номер школы':
        print(f'{ima_pol}, укажите номер школы')
        school_number = input()
        return school_number
    elif question == 'укажите полный номер класса':
        print(f'{ima_pol}, укажите полный номер класса')
        class_num = input()
        return class_num
    else:
        print(f'{ima_pol}, укажите что-нибудь ещё')
        chto_nibyd = input()


name = polite_input('Как вас зовут')
age = polite_input('укажите возраст')
school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')
chto_nibyd = polite_input('укажите что-нибудь ещё')
# Пётр
# 16
# 1
# 9Б
# абракадабра
