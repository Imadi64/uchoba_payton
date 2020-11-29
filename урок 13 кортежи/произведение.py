quantity = int(input())
list_number = [int(input()) for _ in range(quantity)]
number  = int(input())
print('ДА' if [i for i in list_number if number/i in list_number] else 'НЕТ')
