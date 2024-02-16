# >>> s = [1, 2, 3, 4]
# >>> t = iter(s)
# >>> next(s)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'list' object is not an iterator

# >>> next(t)
# 1

# >>> next(t)
# 2

# >>> iter(s)
# <list_iterator object at 0x7f2912345678>

# >>> next(iter(s))
# 1

# >>> next(iter(s))
# 1

# >>> u = t
# >>> next(u)
# 3

# >>> next(t)
# 4

# >>> next(t)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# >>> r = range(6)
# >>> r_iter = iter(r)
# >>> next(r_iter)
# 0

# >>> [x + 1 for x in r]
# [1, 2, 3, 4, 5, 6]

# >>> [x + 1 for x in r_iter]
# []

# >>> next(r_iter)
# 1

# >>> map_iter = map(lambda x : x + 10, range(5))
# >>> next(map_iter)
# 10

# >>> next(map_iter)
# 11

# >>> list(map_iter)
# [12, 13, 14]

# >>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
# ...     print(e)
# 1000
# 1004

# >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
# [5, 7, 9]

# >>> for e in zip([10, 9, 8], range(3)):
# ...   print(tuple(map(lambda x: x + 2, e)))
# (12, 2)
# (11, 3)
# (10, 4)