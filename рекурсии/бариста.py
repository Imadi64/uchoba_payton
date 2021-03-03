ingredients = [1, 2, 3]


def choose_coffee(*preference):
    vidi_coffe = {"Эспрессо": [1, 0, 0],
                  "Капучино": [1, 3, 0],
                  "Маккиато": [2, 1, 0],
                  "Кофе по-венски": [1, 0, 2],
                  "Латте Маккиато": [1, 2, 1],
                  "Кон Панна": [1, 0, 1]}
    kof_zerna, moloko, slivki = ingredients
    a = []
    if kof_zerna < 0:
        print("К сожалению, не можем предложить Вам напиток")
    for i in preference:
        if i in vidi_coffe:
            a, b, c = vidi_coffe[i]
            kof_zerna, moloko, slivki =kof_zerna - a, moloko - b, slivki - c

            if kof_zerna <= 0 or moloko <= 0 or slivki <= 0:



choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна")
