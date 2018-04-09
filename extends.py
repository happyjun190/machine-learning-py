class Animal(object):
    def run(self):
        print("Animal is running")

class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    pass

def set_name(self, name):
    self.name = name

Dog.set_name=set_name
dog = Dog()
dog.set_name("110000")
cat = Cat()
dog.run()
print("###########",dog.name)
cat.run()

print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
print(isinstance(dog, Cat))

