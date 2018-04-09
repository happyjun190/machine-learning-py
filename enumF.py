from hello import Hello
from enum import Enum, unique


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    pass
    #print(name, "=>", member, ",", member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun.value)
print(Weekday['Sun'])

#hello = Hello()
#hello.hello("mmmm")

#print(type(hello))

def fn(self, name='world'):
    print('Hello %s' % name)

Hello1 = type('Hello1', (object,), dict(hello=fn)) # 创建Hello class
hello1 = Hello1()
hello1.hello('mmmm')
print(type(hello1))