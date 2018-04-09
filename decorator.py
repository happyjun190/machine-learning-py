def log(func):
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2017-12-11")

now = log(now)

now()



print("#================================")

def outer():
    x=1
    def inner():
        x = 2
        print("x =", x);
    inner()
    print("x =", x)
outer()

print("#================================")


def outer(some_func):
    def inner():
        print("before some_func")
        print(some_func.__name__)
        ret = some_func()
        return ret+1
    return inner

def foo():
    return 1

decorated = outer(foo)
print(decorated())

print("#================================")
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)

def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret

    return checker

@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)
@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)
one = Coordinate(100, 200)
two = Coordinate(300, 200)
print(add(one, two))


add = wrapper(add)
sub = wrapper(sub)

print(sub(one, two))

print("#================================")

def logger(func):
    def inner(*args, **kw):
        print("function name is : %s" % func.__name__)
        print("function's arguments were : %s, %s" % (args, kw))
        return func(*args, **kw)
    return inner

@logger
def foo1(x, y=1):
    return x*y

print(foo1(1,2))