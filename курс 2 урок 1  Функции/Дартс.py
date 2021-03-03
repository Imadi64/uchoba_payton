scoring = {1: [8, 2], 2: [6, 16], 3: [42, 56], 20: [50, 3]}


def score(*a, **k):
    global scoring
    if len(a) == 1:
        if a[0] == 'Яблочко':
            return 50
        else:
            return 25
    else:
        if a[0] == 'Внешнее_кольцо':
            return scoring[a[1]][0]
        else:
            return scoring[a[1]][1]


print(score("Внешнее_кольцо", 1))
