def falling(n, k):
    sum = 1
    while k > 0:
        sum *= n
        n -= 1
        k -= 1
    return sum

print(str(falling(6, 3)))

print(str(falling(4, 3)))

print(str(falling(4, 1)))

print(str(falling(4, 0)))