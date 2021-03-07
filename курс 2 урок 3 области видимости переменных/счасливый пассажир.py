def lucky(ticket):
    def sum_(number):
        number = str(number)
        while len(number) != 6:
            number = '0' + number
        x = list(map(int, number))
        return sum(x[:3]) == sum(x[3:])

    return 'Счастливый' if sum_(ticket) == sum_(lastTicket) else 'Несчастливый'


lastTicket = 123456
print(lucky(100001))


lastTicket = 123321
print(lucky(100001))
