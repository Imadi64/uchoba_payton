print("Привет! Это бот-говорилка. О чем хочешь поговорить?")
otvet = input()
while (otvet != "Пока") and (otvet != "Досвидания") and (otvet != "Прощай"):
    if "животных" in otvet:
        print("Самые милые животные - котики. А вам нравятся котики?")
        otvet = input()
        while (otvet != "Пока") and (otvet != "Досвидания") and (otvet != "Прощай"):
            if ("не" in otvet) or ("Нет" in otvet) or ("бесят" in otvet):
                print("А давайте сменим тему?")
                break
            if ("Да" in otvet) or ("нравятся" in otvet) or ("очень" in otvet):
                print("Когда коты мурчат, они могут вылечить вас!!! Это факт.")
                break
            print("???")
            otvet = input()
    elif "технике" in otvet or "технику" in otvet:
        print()
    elif "спорте" in otvet or "спорт" in otvet:
        print()
    elif "еде" in otvet or "еду" in otvet:
        print()
    elif "туризм" in otvet or "туризме" in otvet:
        print()
    if (otvet == "Пока") and (otvet == "Досвидания") and (otvet == "Прощай"):
        break
    else:
        print("О чем хочешь поговорить?")
        otvet = input()






print("Пока")