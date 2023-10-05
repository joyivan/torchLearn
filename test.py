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
---
AllMoney=0
op=[]
def SaveMoney(money):
    global AllMoney
    AllMoney+=money
    print('saved money')
    op.append('saved money')
def QueryAccount():
    print(f'You have {AllMoney}')
    op.append('query account')
QueryAccount()
SaveMoney(100)
QueryAccount()
print(op)
class Person():
    BirthYear=1982
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printed(self):
        print(f'name is {self.name}')
        print(f'age is {self.age}')
p1=Person('joyivan','42')
p1.printed()

def addNumber(a,b):
    return a+b
def decor(fun):
    def fun1(a,b):
        print(f'the a is {a},b is {b}')
        return fun(a,b)
    return fun1

addNumber=decor(addNumber)
print(addNumber(3,4))
def fun3():
    i=0
    while True:
        if i>100:
            break
        else:
            yield i
            i+=1
a=fun3()
print(type(a))
for i in range(90):
    print(next(a))

'''
import numpy as np
a=np.zeros((3,3,3))
a[0]=np.array([[1,2,0],[0,1,1],[0,2,2]])
a[1]=np.array([[0,2,1],[2,1,0],[2,1,0]])
a[2]=np.array([[1,1,1],[0,1,1],[0,0,1]])
w=np.zeros((3,3,3))
b=np.zeros((3,3,3))
b[0]=np.array([[-1,0,-1],[1,1,-1],[0,0,0]])
b[1]=np.array([[1,0,0],[0,-1,-1],[-1,1,1]])
b[2]=np.array([[0,0,1],[0,0,-1],[-1,-1,1]])
c=np.multiply(a,b)
print(a[0])

print(c.sum())


