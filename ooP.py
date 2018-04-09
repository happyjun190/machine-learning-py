class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError("bad score")

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 60:
            return "B"
        else:
            return "C"

bart = Student("Bart Simpson", 59)
amy = Student("Amy Simpson", 59)
bart.code = "aaaaa";
bart.set_score(99)
print(bart.get_score())
#print(bart.__name)
#print(bart.__score)
print(bart.code)
#print(amy.code)
print(bart.get_grade())
#bart.print_score();
