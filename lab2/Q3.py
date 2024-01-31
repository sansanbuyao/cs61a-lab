# >>> lambda x: x
# <function <lambda> at 0x7f9d5a4c6c10>

# >>> a = lambda x: x
# >>> a(5)
# 5

# >>> (lambda: 3)()
# 3

# >>> b = lambda x, y: lambda: x + y
# >>> c = b(88, 43)
# >>> c
# <function b.<locals>.<lambda> at 0x7f9d5a4c6f70>

# >>> c()
# 131

# >>> d = lambda f: f(4)
# >>> def square(x):
# ...     return x * x
# >>> d(square)
# 16

# >>> higher_order_lambda = lambda f: lambda x: f(x)
# >>> g = lambda x: x * x
# >>> higher_order_lambda(2)(g)
# 4

# >>> higher_order_lambda(g)(2)
# 4

# >>> call_thrice = lambda f: lambda x: f(f(f(x)))
# >>> call_thrice(lambda y: y + 1)(0)
# 3

# >>> print_lambda = lambda z: print(z)
# >>> print_lambda
# <function <lambda> at 0x7f9d5a4c6e60>

# >>> one_thousand = print_lambda(1000)
# 1000

# >>> one_thousand
# None
