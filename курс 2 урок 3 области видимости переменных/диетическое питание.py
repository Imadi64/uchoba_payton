def diet(eat):
    eat = eat.split(', ')
    count = 0
    for i in eat:
        if i in food['диетическое']:
            count += 1
    if float(count) >= len(eat) / 2:
        return 'Так держать, Воин Дракона!'
    else:
        return 'Не ешь столько, По!'


food = {'жирное': ["растительное масло", 'гамбургер'],
        'сладкое': ['печенье', 'чай', 'мёд', 'сахар', 'торт'],
        'мучное': ["печенье"],
        'диетическое': ['творог', 'фрукты', 'каша', 'зелень', 'овощи', 'рис'], }

print(diet("творог"))
print(diet("печенье, чай, сахар, фрукты, мед"))
