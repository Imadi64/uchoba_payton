for _ in range(int(input())):
    lst = input().split()
    if lst[0].lower() == 'не':
        print(' '.join(lst[1:]))
    else:
        print(' '.join(lst))