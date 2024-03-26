def falling(n, k):
    sum = 1
    while k > 0:
        sum *= n
        n -= 1
        k -= 1
    return sum

