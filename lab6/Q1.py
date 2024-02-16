# >>> s = [6, 7, 8]
# >>> print(s.append(6))
# None

# >>> s
# [6, 7, 8, 6]

# >>> s.insert(0, 9)
# >>> s
# [9, 6, 7, 8, 6]

# >>> x = s.pop(1)
# >>> s
# [9, 7, 8, 6]

# >>> s.remove(x)
# >>> s
# [9, 8, 6]

# >>> a, b = s, s[:]
# >>> a is s
# True

# >>> b == s
# True

# >>> b is s
# False

# >>> s = [3]
# >>> s.extend([4, 5])
# >>> s
# [3, 4, 5]

# >>> s.extend([s.append(9), s.append(10)])
# >>> s
# [3, 4, 5, None, None]