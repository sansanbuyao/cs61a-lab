def div_by_primes_under_no_lambda(n):
    def checker(x):
        return False

    i = 2
    while i < n:
        if not checker(i):
            def outer(func):
                def inner(y):
                    return y % i == 0
                return inner
            checker = outer(i)
        i += 1

    return checker
