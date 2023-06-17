class Animal():
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class babydog(Dog):
    def cry(self):
        print("crying")
c=babydog()
c.eat()
c.bark()
c.cry()


