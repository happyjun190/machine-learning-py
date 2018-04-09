def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax+n
            print(ax)
        return ax
    return sum

f = lazy_sum(1,2,3,4,5,6,7,8,9)


f()


print(list(range(1,4)))

f=abs
print(f.__name__)