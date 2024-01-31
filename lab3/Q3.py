import math

def nearest_two(x):
    power = int(math.log2(x))
    lower_power = 2 ** power
    upper_power = 2 ** (power + 1)

    if abs(x - lower_power) <= abs(x - upper_power):
        return lower_power
    else:
        return upper_power
