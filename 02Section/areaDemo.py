import math
radius = float(input("Enter the radius : "))
print (radius)

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("The area of radius is  : ",round(area,2))
print("The area of circumference is  : ",circumference)