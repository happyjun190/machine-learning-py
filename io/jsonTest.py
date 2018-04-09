import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
class Teacher(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2Dict(student):
    return {
        'name':student.name,
        'age':student.age,
        'score':student.score
    }
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])


student = Student('Student', 20, 90)
teacher = Teacher('Teacher', 20, 90)
print(json.dumps(student, default=student2Dict))
print(json.dumps(teacher, default=lambda obj : obj.__dict__))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2Student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)