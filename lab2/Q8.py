
def cycle(f1, f2, f3):
    def g(n):
        def h(x):
            if n == 0:
                return x
            elif n == 1:
                return f1(x)
            elif n == 2:
                return f2(f1(x))
            elif n == 3:
                return f3(f2(f1(x)))
            else:
                result = x
                for _ in range(n):
                    if _ % 3 == 0:
                        result = f1(result)
                    elif _ % 3 == 1:
                        result = f2(result)
                    else:
                        result = f3(result)
                return result
        return h
    return g
