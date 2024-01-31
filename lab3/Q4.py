def make_repeater(func, n):
    def repeated_func(x):
        result = x
        for i in range(n):
            result = func(result)
        return result
    return repeated_func


