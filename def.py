class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        pass
class Dog(Animal):
    def talk(self):
        print("woof")
class cat(Animal):
    def talk(self):
        print("meawu")
c=cat('kingini')
c.talk()
d=Dog('dooby')
d.talk()