def late(now, classes, bus):
    now = now.split(':')
    now[0], now[-1] = int(now[0]), int(now[-1])
    _now = now[0] * 60 + now[-1]
    classes = classes.split(':')
    classes[0], classes[-1] = int(classes[0]), int(classes[-1])
    _classes = (classes[0] * 60 + classes[-1]) - _now
    _answ = []
    for time in bus:
        if time >= 5 and time <= _classes - 15:
            _answ.append(time)
    if _answ == []:
        return 'Опоздание';
    else:
        return 'Выйти через ' + str(max(_answ) - 5) + ' минут';
print(late('9:00','10:00',[5,15,25]))
print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('9:20', '9:35', [4, 25, 30]))
