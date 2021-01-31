n = int(input())
s = [int(input()) for i in range(n)]
p = int(input())
q = int(input())
print(sum(s[p - 1:q]))
