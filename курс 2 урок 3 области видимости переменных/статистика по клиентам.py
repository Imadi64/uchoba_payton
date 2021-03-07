def get_transactions(t):
    if t == 'print_it':
        for i in dcttime:
            print(dcttime[i], i, dctmoney[i])
        return
    where = t[t.find('-') + 1:t.find(':')]
    how_many = int(t[t.find(':') + 1:])
    if where in dcttime:
        dcttime[where] += 1
        dctmoney[where] += how_many
    if where not in dcttime:
        dcttime[where] = 1
        dctmoney[where] = how_many


dcttime = {}
dctmoney = {}


get_transactions('880005553535-перевод:100')
get_transactions('111111111-перевод:1000')
get_transactions('880005553535-оплата_жкх:10000')
get_transactions('89065664312-перевод:50000000')
get_transactions('print_it')