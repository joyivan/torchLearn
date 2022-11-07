def fun1(ff):
    def fun2(a):
        a=a+2
        return ff(a)
    return fun2



@fun1
def main(num):
    a=1
    for i in range(1,num+1):
        a*=i
    return a

print(main(10))