import sys
sys.path.append('..')
from d2.pp2 import person
from d2.pp2 import call911
print('I am pp1 file')
def call120():
    print('call 120! HELP!!!There is a patient')
class car():
    def __init__(self,name):
        print('car init finish!')
        self.name=name
    def run(self):
        print(f'{self.name} is runing!')

if __name__ =='__main__':
    car1=car('benz')
    p1=person('joyivan')
    p1.cry()
    call911()