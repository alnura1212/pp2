import math
class Point:
    def show(self):
        self.x1=int(input("x1= "))
        self.y1=int(input("y1= "))
    def move(self):
        self.x2=int(input("x2= "))
        self.y2=int(input("y2= "))
    def dist(self):
        self.AB=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        print("distance= ", self.AB)

p1=Point()
p1.show()
p1.move()
p1.dist()