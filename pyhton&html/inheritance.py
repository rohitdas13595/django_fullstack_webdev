class Animal():
    def __init__(self):
        print("Animal CREATED ")
    def whoAmI(self):
        print("animal")
    def eat(self):
        print('EATIING')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog CREATED")
    def sound(self):
        print("Barking")

mydog =Dog()
mydog.whoAmI()
mydog.eat()
mydog.sound()
