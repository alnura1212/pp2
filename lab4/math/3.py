import math

n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
a = l / 2 * (math.tan(math.pi/n))
area = (n * l * a) / 2
print("The area of the polygon is: ", math.ceil(area))