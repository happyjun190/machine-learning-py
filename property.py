class Student(object):
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must an integer")
        elif score <0 or score >100:
            raise ValueError("score must between 0 and 100")
        self.__score = score
s = Student()
s.set_score(10)
print(s.get_score())

class Student1(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must an integer")
        elif score <0 or score >100:
            raise ValueError("score must between 0 and 100")
        self.__score = score

class Student2(object):

    def __init__(self, name):
        self.__name = name

    def __str__(self) :
        return "Student object (name:%s)" % self.__name

    __repr__ = __str__

print(Student2("Mark").__repr__)


class Fib(object):
    def __init__(self):
        self.__a, self.__b = 0, 1   # 初始化两个计数器a，b

    def __iter__(self):
        return self                 # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a+self.__b
        if self.__a > 100000:
            raise StopIteration()
        return self.__a

    def __getitem__(self, n):
        if isinstance(n, int):     # n是索引
            a, b = 0, 1
            for x in range(n):
                a, b = b, a+b
            return a
        elif isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x> start:
                    L.append(a)
                a, b = b , a+b
            return L


for n in Fib():
    print(n)

print(Fib()[1])

print(Fib()[1:10])