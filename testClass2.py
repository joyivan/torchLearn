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
def add1(time):
   def add3(a):
       print(time)

       #@functools.wraps(a)
       def add2(c,b):
           print(id(a))
           return a(c,b)

       return add2
   return add3
@add1(time=10)
def add(a,b):
    return a+b
c=add(1,2)
print(add.__name__)
print(c)