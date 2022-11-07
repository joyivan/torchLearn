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
