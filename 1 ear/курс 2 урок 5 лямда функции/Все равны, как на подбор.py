def same_by(f, arr):
    return all(not f(i) for i in arr)


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


print()
print()


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')