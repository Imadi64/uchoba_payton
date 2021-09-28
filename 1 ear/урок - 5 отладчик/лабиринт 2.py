a = 0
while a == 0:

    print("Вы находитесь в пещере на развилке. "
          "Вы можете пойти \"налево\", \"направо\" или \"прямо\". "
          "Введите одно из слов в кавычках для выбора.")
    razvilka_1 = input()
    while (razvilka_1 != "прямо") and (razvilka_1 != "направо") and (razvilka_1 != "налево"):
        print("Вы ввели неправильно!!!")
        razvilka_1 = input()
    if razvilka_1 == "налево":
        print("вы упали в яму с шипами!")
        a = 1
        break
    elif razvilka_1 == "прямо":
        print("Вас укусила ядовитая змея!")
        a = 1
        break
    elif razvilka_1 == "направо":

        while a == 0:

            print("Вы попали в новую комнату")
            print("Вы можете пойти \"налево\", \"направо\", \"прямо\" или \"вернуться\"."
                  "Введите одно из слов в кавычках для выбора.")
            razvilka_2 = input()
            while (razvilka_2 != "прямо") and (razvilka_2 != "направо") and (razvilka_2 != "налево") \
                    and (razvilka_2 != "вернуться"):
                print("Вы ввели неправильно!!!")
                razvilka_2 = input()
            if razvilka_2 == "налево":
                print("Вы попали в комнату и вас убил призрак!")
                a = 1
                break
            elif razvilka_2 == "вернуться":
                break
            elif razvilka_2 == "прямо":
                print("Вы попали в новую комнату с монстром.")
                print("у вас есть выбор, \"бежать\" или \"драться\"")
                razvilka_s_mon = input()
                while (razvilka_s_mon != "бежать") and (razvilka_s_mon != "драться"):
                    print("Вы ввели неправильно!!!")
                    razvilka_s_mon = input()
                if razvilka_s_mon == "бежать":
                    print("Вы бежали сломя голову и споткнулись и упали.")
                    print("Вас догнал монстр и убил.")
                    a = 1
                    break
                elif razvilka_s_mon == "драться":
                    print("Монстр победил. Надо было бежать.")
                    a = 1
                    break
            elif razvilka_2 == "направо":

                while a == 0:

                    print("Вы попали в новую комнату и видете три двери.")
                    print("Вы можете пойти \"налево\", \"направо\", \"прямо\" или \"вернуться\"."
                          "Введите одно из слов в кавычках для выбора.")
                    razvilka_3 = input()
                    while (razvilka_3 != "прямо") and (razvilka_3 != "направо") and (razvilka_3 != "налево") \
                            and (razvilka_3 != "вернуться"):
                        print("Вы ввели неправильно!!!")
                        razvilka_3 = input()
                    if razvilka_3 == "налево":
                        print("Вы попали в бесконечно длинный коридор.")
                        print("Вы решились пойти туда и умерли от истощения.")
                        a = 1
                        break
                    elif razvilka_3 == "вернуться":
                        break
                    elif razvilka_3 == "направо":
                        print("Вы решили пойти направо.")
                        print("Урааа. Видны лучи солнца.")
                        print("Победа!!!")
                        a = 1
                        break
                    elif razvilka_3 == "прямо":
                        print("Вас съела 3-х метровая венерина мухоловка.")
                        a = 1
                        break
print("Начните игру заново.")
