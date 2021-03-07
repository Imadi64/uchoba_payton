def tribonacci(n):
    if (n == 2):
        return 1
    elif (n < 2):
        return 0
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(1))
print(tribonacci(2))
print(tribonacci(4))
print(tribonacci(6))
print(tribonacci(8))
print(tribonacci(10))
print(tribonacci(12))
print(tribonacci(100))
