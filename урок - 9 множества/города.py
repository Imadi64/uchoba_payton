s1 = input().lower()
while True:
    s2 = input().lower()
    if s1[-1] != s2[0]:
        print(s2)
        break
    s1 = s2

