print("Привет! Это бот-говорилка. О чем хочешь поговорить?")
otvet = input().lower()
while (otvet != "пока") and (otvet != "досвидания") and (otvet != "прощай"):

    if "животных" in otvet:
        print("Самые милые животные - котики. А вам нравятся котики?")
        otvet = input().lower()
        while (otvet != "пока") and (otvet != "досвидания") and (otvet != "прощай"):
            if ("не" in otvet) or ("нет" in otvet) or ("бесят" in otvet):
                print("А давайте сменим тему?")
                break
            if ("да" in otvet) or ("нравятся" in otvet) or ("очень" in otvet):
                print("Когда коты мурчат, они могут вылечить вас!!! Это факт.")
                break
            print("Неособо понял ваш ответ?")
            otvet = input()

    elif "технике" in otvet or "технику" in otvet:
        print("Техника вокруг вас, наример я. Вы часто пользуетесь гаджетами?")
        otvet = input().lower()
        while (otvet != "пока") and (otvet != "досвидания") and (otvet != "прощай"):
            if ("да" in otvet) or ("часто" in otvet) or ("почти всегда" in otvet):
                print("Сторайтесь сидеть немного поменьше, предлагаю сходить на улицу.")
                break
            elif ("нет" in otvet) or ("редко" in otvet) or ("не " in otvet):
                print("Техника полезна, но хорошо, что вы залипаете в интернене те так часто.")
                break
            print("Неособо понял ваш ответ?")
            otvet = input().lower()

    elif "спорте" in otvet or "спорт" in otvet:
        print("Часто занимаетесь дома или в спортивном зале?")
        otvet = input().lower()
        while (otvet != "пока") and (otvet != "досвидания") and (otvet != "прощай"):
            if ("да" in otvet) or ("часто" in otvet) or ("каждый день" in otvet):
                print("Это класно и полезно, но неперегружайтесь!!! Это вредно.")
                break
            elif ("нет" in otvet) or ("редко" in otvet) or ("ниразу не ходил" in otvet) or ("не " in otvet):
                print("Советую вам делать физические упражнения по чаще. Тело будет красивое, здоровое и заколенное.")
                break
            print("Неособо понял ваш ответ?")
            otvet = input().lower()

    elif "еде" in otvet or "еду" in otvet:
        print("Вам нравится фастфуд?")
        otvet = input().lower()
        while (otvet != "пока") and (otvet != "досвидания") and (otvet != "прощай"):
            if ("да" in otvet) or ("очень" in otvet) or ("жить без него немогу" in otvet):
                print("Я его тоже люблю. Но много есть ненадо лучше раз в неделю и физ. упражнения для красивого тела.")
                break
            elif ("нет" in otvet) or ("не " in otvet) or ("он вреден" in otvet):
                print("Ок, но мне он нравится особенно пицца.")
                break
            print("Неособо понял ваш ответ?")
            otvet = input().lower()

    elif "туризм" in otvet or "туризме" in otvet:
        print("Вам нравится альпинизм?")
        otvet = input().lower()
        while (otvet != "пока") and (otvet != "досвидания") and (otvet != "прощай"):
            if ("не " in otvet) or ("нет" in otvet) or ("я предрочитаю другой вид спорта" in otvet):
                print("Понятно. Мне больше нравится альпинизм не на горе а на спортивных площадках.")
                break
            elif ("да" in otvet) or ("очень" in otvet) or ("часто им занимался" in otvet):
                print("Круть!!!")
                break
            print("Неособо понял ваш ответ?")
            otvet = input().lower()
    if (otvet == "пока") and (otvet == "досвидания") and (otvet == "прощай"):
        break
    else:
        print("О чем хочешь поговорить?")
        otvet = input().lower()






print("Пока")