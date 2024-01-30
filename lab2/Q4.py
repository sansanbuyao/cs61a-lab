#Write a function that takes in two single-argument functions,fandg, andreturns anotherfunctionthat has a single parameterx. 
#The returnedfunction should returnTrueiff(g(x))is equal tog(f(x)). 
#You canassume the output ofg(x)is a valid input forfand vice versa.
#Try to use thecomposerfunction defined below for more HOF practice, or alambda expression for more lambda practice.

add_one = lambda x: x + 1        # adds one to x
square = lambda x: x**2          # squares x [returns x^2]
def composer(f, g):
    def h(x):
        return f(g(x))
    return h

a1 = composer(square, add_one)
print(a1(4))


def composite_identity(f, g):
    return lambda x: f(g(x)) == g(f(x))

b1 = composite_identity(square, add_one)
print(b1(0))  # 输出：True
print(b1(4))  # 输出：False
