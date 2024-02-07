class Shape:
    def area(self):
        self.a=0
        print ("area: ", self.a)
class Rectangle(Shape):
    def __init__(self):
        self.length=float(input("length: "))
        self.width=float(input("width: "))
    def area(self):
        a=self.length*self.width
        print("area: ", a)
p1=Shape()
p1.area()

p2=Rectangle()
p2.area()