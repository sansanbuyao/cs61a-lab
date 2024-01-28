def xk(c, d):
     if c == 4:
         return 6
     elif d >= 4:
         return 6 + 7 + c
     else:
         return 25
print(str(xk(10, 10)))

print(str(xk(10, 6)))

print(str(xk(4, 6)))

print(str(xk(0, 0)))

#--------------------------------------------------------------------
def how_big(x):
     if x > 10:
         print('huge')
     elif x > 5:
         return 'big'
     elif x > 0:
         print('small')
     else:
         print("nothing")

# print(how_big(7))

# print(how_big(12))

# print(how_big(1))

# print(how_big(-1))
         
how_big(7)

how_big(12)

how_big(1)

how_big(-1)

#------------------------------------------------------------------
n = 3
while n >= 0:
    n -= 1
    print(n)

positive = 28
while positive and positive>0:
    print("positive?")
    positive -= 3

negative = -12
while negative and negative < 0: 
    if negative + 6:
        print(negative)
    negative += 3
