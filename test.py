'''
# region Description
class Animal():
    def __init__(self,name):
       self.name=name

    def scream(self):
        print('sound from animal')
class Dog(Animal):
    def scream(self):
        print('wof!!!')
class Cat(Animal):
    def scream(self):
        print('Miao!!!')
class person():

    def __init__(self,name):
        self.name=name
    def touchAnimal(self,animal):
        animal.scream()

if __name__=='__main__':
    person1=person('li4')
    cat=Cat('cc')
    dog=Dog('dd')
    person1.touchAnimal(dog)
class BaseClass():
    def __init__(self,value):
        self.value=value
        print('In BaseClass,value is ',self.value)

class class1(BaseClass):
    def __init__(self,value):
        super(class1,self).__init__(value)
        self.value=value*2
        print('In Class1,value is ',self.value)

class class2(BaseClass):
    def __init__(self,value):
        super(class2,self).__init__(value)
        self.value=value+2
        print('In Class2,value is ', self.value)


class OneWay(class1,class2):
    def __init__(self,value):
        super(OneWay,self).__init__(value)
        print(self.value)
foo=OneWay(3)
print(OneWay.__mro__)
class A:
  def save(self):
      print('In A')

class B(A): pass

class C(A):
  def save(self):
      print('In C')

class D(B, C): pass
d=D()
d.save()
(<class '__main__.OneWay'>, <class '__main__.class1'>,
<class '__main__.class2'>, <class '__main__.BaseClass'>, <class 'object'>)

class BaseClass():
    def __init__(self,value):
        self.value=value
        print('In BaseClass,value is ',self.value)

class class1(BaseClass):
    def __init__(self,value):
        self.value=value+2
        print('In Class1,value is ',self.value)

class class2(BaseClass):
    def __init__(self,value):
        self.value=value*5
        print('In Class2,value is ', self.value)


class OneWay(class1,class2,BaseClass):
    def __init__(self,value):
        BaseClass.__init__(self,value)
        class1.__init__(self,value)
        class2.__init__(self,value)
foo=OneWay(3)
print(foo.value)
'''

def func1(func):
    def newfunc():
        print(1)
        func()
        print(2)
    return newfunc

def func2(func):
    def newfunc1():
        print(4)
        func()
        print(5)
    return newfunc1

@func1
@func2
def func():
    print(3)


func()