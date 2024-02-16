def count_occurrences(t, n, x):
    count = 0
    for i in range(n):
        try:
            element = next(t)
        except StopIteration:
            break
        if element == x:
            count += 1
    return count
