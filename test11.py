def fun1(papa):
        def fun3(f1):
            def fun2(a,b):
                if papa==1:
                    a=a**2
                    b=b**2
                elif papa==0:
                    a=abs(a)
                    b=abs(b)
                return f1(a,b)
            return fun2
        return fun3

@fun1(1)
def add(a,b):
    return a+b

@fun1(0)
def minus(a,b):
    return a-b

c=add(2,3)
print(c)
c=minus(-3,2)
print(c)
