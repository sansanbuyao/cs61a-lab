def get_k_run_starter(n, k):
    n_str = str(n)
    count = 0
    prev_digit = None

    for digit in n_str:
        if prev_digit is None or digit > prev_digit:
            count += 1
            if count == k:
                return int(digit)
        else:
            count = 1
        prev_digit = digit
    
    return None
