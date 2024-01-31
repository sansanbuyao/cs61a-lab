# >>> True and 13
# 13

# >>> False or 0
# 0

# >>> not 10
# False

# >>> not None
# True


# >>> True and 1 / 0
# ZeroDivisionError: division by zero

# >>> True or 1 / 0
# ZeroDivisionError: division by zero

# >>> -1 and 1 > 0
# True

# >>> -1 or 5
# -1

# >>> (1 + 1) and 1
# 1

# >>> print(3) or ""
# 3


# >>> def f(x):
# ...     if x == 0:
# ...         return "I am zero!"
# ...     elif x > 0:
# ...         return "Positive!"
# ...     else:
# ...         return ""
# >>> 0 or f(1)
# Positive!

# >>> f(0) or f(-1)
# ""

# >>> f(0) and f(-1)
# I am zero!