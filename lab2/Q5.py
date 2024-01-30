#Consider the following implementations ofcount_fivesandcount_primes:


def count_cond(condition):
    def count_numbers(N):
        count = 0
        for i in range(1, N+1):
            if condition(N, i):
                count += 1
        return count
    return count_numbers


# 示例 - 计算满足条件的数字总数
count_numbers_func = count_cond(lambda n, i: i % 2 == 0)  # 计算偶数的数量

# 调用自定义的计数函数
result = count_numbers_func(10)  # 计算从1到10中的偶数数量

print(result)  # 输出：5
