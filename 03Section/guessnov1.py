import random

number = random.randint(1,10)

guess =  int(input("please enter no: "))

while True :
    if(number == guess) :
        break
    else :
        guess =  int(input("try again please enter new no: "))
print("u guessed right no :",guess)