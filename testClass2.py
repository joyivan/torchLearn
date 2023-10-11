import sys
#def fun(a):
#    print('in fun')
#    def fun1(b):
#        print('in fun1')
#        return a+b
#    return fun1
#
#mm=fun(1)
#c=mm(2)
#print(c)
import functools
#def add1(time):
#   def add3(a):
#       print(time)
#
#       #@functools.wraps(a)
#       def add2(c,b):
#           print('a name is',id(a))
#           return a(c,b)
#
#       return add2
#   return add3
#@add1(time=10)
#def add(a,b):
#    return a+b
#c=add(1,2)
#print(add.__name__)
#print(c)
class student():
    NoOfStu=0
    def __new__(cls, *args, **kwargs):
       try:
          if cls.NoOfStu<10:
              print(cls.NoOfStu)
              return super().__new__(cls)
          else:
              print('limit 10')
              raise ValueError("fail to create student")
       except ValueError as e:
          sys.exit()
    def __init__(self):
        student.NoOfStu+=1

a={}
for i in range(9):
    temp=student()
    a.update({i:temp})
print(len(a))
print(a.keys())
class univer():
    instance=None
    def __new__(cls, *args, **kwargs):
        if univer.instance is None:
              univer.instance=super().__new__(cls)
              return univer.instance
        else:
            return univer.instance
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def driver(self):
        print(self.a,'|',self.b)
a=univer(1,2)
b=univer(3,4)
print('eeee')
print(a,b)
print(a.driver(),b.driver())

'''
class A:
    def foo(self):
        print("A foo")

class B(A):
    def foo(self):
        print("B foo")

class C(A):
    def foo(self):
        print("C foo")

class D(B, C):
    def foo(self):
        super().foo()  # 调用父类 A 的 foo() 方法

d = D()
d.foo()
print('-'*40)
class A:
    def foo(self):
        print("A foo")

class B(A):
    def foo(self):
        super().foo()
        print("B foo")

class C(A):
    def foo(self):
        super().foo()
        print("C foo")

class D(B, C):
    def foo(self):
        super().foo()
        print("D foo")
d=D()
print(D.mro())
'''