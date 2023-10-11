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
for i in range(13):
    temp=student()
    a.update({i:temp})
print(len(a))
print(a.keys())
