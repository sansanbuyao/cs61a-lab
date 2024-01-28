#编写一个函数，它接受一个非负整数并对其数字求和
def sum_digits(y):
    sum=0
    while y>0:
        sum+=y%10
        y//=10
    return sum

b=sum_digits(10) # 1 + 0 = 1
print(str(b))

c=sum_digits(4224) # 4 + 2 + 2 + 4 = 12
print(str(c))

d=sum_digits(1234567890)
print(str(d))

a = sum_digits(123)    
print(str(a))