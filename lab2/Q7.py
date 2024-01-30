#Write a function that takes in two numbers and returns the smallest number thatis a multiple of both.
def multiple(a, b):
    
    # 计算最大公约数
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # 计算最小公倍数
    lcm = abs(a * b) // gcd(a, b)

    return lcm

