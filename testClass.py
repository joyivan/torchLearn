class ani:
    total=0
    def __new__(cls, *args, **kwargs):
        if ani.total<10:
            return object.__new__(cls)
        else:
            print('sorry,limit class number')
    def __init__(self):
        ani.total+=1
        print(f'U are the {self.total} animal in the world')
        print()
a={}
for i in range(30):
    temp=ani()
    a.update({i:temp})

print(len(a))
class Animal:
    def __init__(self,aname):
        self.name = aname
    def enjoy(self):
        print("动物在叫")

class Cat(Animal):
    def enjoy(self):
        print(self.name,"喵喵喵")

class Dog(Animal):
    def enjoy(self):
        print(self.name,"汪汪汪")

class Person:
    def __init__(self,id,name):
        self.name = name
        self.id = id
    def drive(self,ani):
        ani.enjoy()

cat = Cat("Mikey")
dog = Dog("Dahuang")
person = Person("张三",9)
person.drive(cat)
person.drive(dog)
