total = []
for i in range(int(input())):
    total.append(input())
search = input()
for i in total:
    if search in i:
        print(i)
