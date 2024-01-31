def apply_twice(func):
    def applied_twice(x):
        return func(func(x))
    return applied_twice
