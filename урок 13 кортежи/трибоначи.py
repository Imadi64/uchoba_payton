n = int(input())
f1, f2, f3 = 0, 0, 1
for i in range(n):
    print(f3, end=" ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3
    
