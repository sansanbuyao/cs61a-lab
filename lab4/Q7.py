def summation(n, term):
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n - 1, term)
