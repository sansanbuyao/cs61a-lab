def double_eights(n):
    while n > 0:
        last_digit = n % 10
        n //= 10
        if last_digit == 8 and n % 10 == 8:
            return True
    return False
