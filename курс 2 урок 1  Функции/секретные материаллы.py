def print_document(pages):
    for i in pages:
        a = i.split(" ")
        if a[0] == "Секретно":
            print("Дальнейшие материалы засекречены")
            break
        elif pages[-1] == i:
            print(i)
            print("Напечатано без купюр")
        else:
            print(i)


print_document(["Пустой трёп", "который", "никому не интересен"])
