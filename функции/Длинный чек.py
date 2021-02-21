list_product = []
number_chek = 1
price = 0


def add_item(item_name, item_cost):
    global price, list_product
    price += item_cost
    list_product.append(item_name + " - " + str(item_cost))


def print_receipt():
    global list_product, price, number_chek
    if len(list_product) != 0:
        print(f"Чек {number_chek}. Всего предметов: {len(list_product)}")
        for i in list_product:
            print(i)
        print(f"Итого: {price}")
        print("-----")
        list_product = []
        number_chek += 1
        price = 0


add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()
