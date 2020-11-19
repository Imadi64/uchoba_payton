value = None
result = 0
discount = 0.05
start_discount = 1000
while True:
    value = float(input())
    if value == -1.0:
        break
    else:
        result += value if value <= start_discount else value - value * discount
print(result)
