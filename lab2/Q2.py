>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
beets

>>> chocolate
<function cake.<locals>.pie at 0x7f9d5a4c63a0>

>>> chocolate()
sweets
'cake'

>>> more_chocolate, more_cake = chocolate(), cake
beets
sweets

>>> more_chocolate
'cake'

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
30

>>> snake(10, 20)()
sweets
'cake'

>>> cake = 'cake'
>>> snake(10, 20)
<function cake at 0x7f9d5a4b9790>
