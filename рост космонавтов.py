rost = input()
cosmonavti = 0
max_rost = 0
min_rost = 1000
while rost != "!":
    if 150 < int(rost) <= 190:
        cosmonavti += 1
        if int(rost) > max_rost:
            max_rost = int(rost)
        if int(rost) < min_rost:
            min_rost = int(rost)
    rost = input()
print(cosmonavti)
print(min_rost, max_rost)