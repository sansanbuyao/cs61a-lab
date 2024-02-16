def repeated(t, k):
    assert k > 1

    prev_value = None
    count = 0

    while True:
        try:
            value = next(t)
        except StopIteration:
            break

        if value == prev_value:
            count += 1
            if count == k - 1:
                return value
        else:
            count = 1

        prev_value = value

    return None
