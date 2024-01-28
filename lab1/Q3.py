#编写函数divisible_by_k取正整数的n个和k。它打印所有小于或等于的正整数n个可以被k从最小到最大。然后，它返回打印了多少个数字。
def divisible_by_k(n, k):
    count=0
    i=1
    while i<=n:
        if i%k==0:
           count+=1
        i+=1   
    return count        

a = divisible_by_k(10, 2)
print(str(a))

b = divisible_by_k(3, 1)
print(str(b))

c = divisible_by_k(6, 7) 
print(str(c))