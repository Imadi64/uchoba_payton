print('Добро пожаловать в интернет-банк!')
print('У нас фантастические процентные ставки!')
print('Для вкладов до 10 тысяч ₽ включительно прибыль составит 10%,')
print('для вкладов на сумму до 100 тысяч включительно - 20%,')
print('для более 100 тысяч - 30%!')
print('На какую сумму желаете сделать вклад?')
rybli = float(input())
if rybli <= 10000:
    rybli *= 1.1
elif rybli <= 100000:
    rybli *= 1.2
elif rybli > 100000:
    rybli *= 1.3
print('Вы получаете', rybli, '₽, поздравляем!')

