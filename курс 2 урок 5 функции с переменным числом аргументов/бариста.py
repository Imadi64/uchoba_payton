ingredients = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],
              'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
              'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}


def choose_coffee(*preferences):
    for i in preferences:
        if ingredients[i][0] <= ingredients[0] and ingredients[i][1] <= ingredients[1] \
                and ingredients[i][2] <= ingredients[2]:
            ingredients[0] -= ingredients[i][0]
            ingredients[1] -= ingredients[i][1]
            ingredients[2] -= ingredients[i][2]
            return i
    return 'К сожалению, не можем предложить Вам напиток'


ingredients = []





ingredients = [1, 2, 3]
print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна"))
print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна"))
