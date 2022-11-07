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
for i in range(10):
    temp=ani()
    a.update({i:temp})
print(a[9])

