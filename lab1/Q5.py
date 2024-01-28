def double_eights(n):
    lst = []
    while n > 0:
        lst.insert(0, n % 10)
        n //= 10
    
    for i in range(len(lst)-1):
        if lst[i] == 8 and lst[i+1] == 8:
            return True
    return False


print(double_eights(88))          
print(double_eights(2882))        
print(double_eights(880088))      
print(double_eights(12345))      
print(double_eights(80808080))    
