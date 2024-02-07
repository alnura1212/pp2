class Shape:
    def area(self):
        self.a=0
        print ("area: ", self.a)
class Square(Shape):
    def __init__(self):
        self.length=float(input("length: "))
    def area(self):
        a=self.length**2
        print("area: ",a)

p1=Shape()
p1.area()

p2=Square()
p2.area()