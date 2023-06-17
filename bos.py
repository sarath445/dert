class Circle():
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getcircumference(self):
        return 2*3.14*self.radius
a=int(input("enter radius"))
b=int(input("enter radius"))
c1=Circle(a)
c2=Circle(b)
print(c1.getArea())
print(c1.getcircumference())
print(c2.getArea())
print(c2.getcircumference())



