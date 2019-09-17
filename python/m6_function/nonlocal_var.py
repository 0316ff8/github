# P98
'''
def func():
    x = 10
    def get_x():
        return x
    def set_x():
        x = n
    return get_x(), set_x()

getX, setX = func()
print(getX())
setX(20)
print(getX())
'''

def func1():
    x = 10

    def get_x():
        return x

    def set_x(n):
        nonlocal x
        x = n   #x與外部x=10對調
    return get_x, set_x

get_x, set_x = func1()
print(get_x())
set_x(20)
print(get_x())
