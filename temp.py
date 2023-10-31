class stu():
    def __init__(self,iid,name,age):
        self.iid=iid
        self.name=name
        self.age=age
    def modyFiled(self,field,value):

        if field=='age':
            self.age=value
        elif field=='iid':
            self.iid=value
        elif field=='name':
            self.name=value

    def printStu(self):
            print(self.iid,self.name,self.age)
            print(self)

stu1=stu(1,'jack',20)
stu1.printStu()
stu1.modyFiled('age',24)
stu1.printStu()
#gitee
