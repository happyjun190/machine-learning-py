from inspect import isgeneratorfunction
def f(x):
    return x%2==1

l1 = list(filter(f, list(range(100))))
#print(l1)

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
#for n in fab(10):
#    print(n)

print(isgeneratorfunction(fab))