#Draw the environment diagram that results from executing the code below.

n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)


Global Frame:
------------------------
|     n = 7            |
|     f -------------> | <function: f>
|     g -------------> | <function: g>
------------------------

f Frame:
------------------------
|     x                |
|     n = 8            |
------------------------

g Frame:
------------------------
|     x                |
|     n = 9            |
|     h -------------> | <function: h>
------------------------

h Frame:
------------------------
|                      |
------------------------
