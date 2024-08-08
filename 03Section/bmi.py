height = float(input("enter height in meters of persion:"))
weight = float(input("enter weight in kg of persion:"))

bmi = weight / (height ** 2)

print("Body mass index is :", round(bmi,2))

if(bmi <=18.5):
    print("underweight")
elif(bmi >18.5 and bmi <=24.9):
    print("normal weight")
elif(bmi > 24.9 and bmi <=29.9):
    print("overweight")
else:
    print("obesity")