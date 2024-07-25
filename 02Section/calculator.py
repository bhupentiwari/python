def calculator():
    num1 =  float(input("Enter number 1 : "))
    num2 =  float(input("Enter number 2 : "))
    opr = input("Enter operation (+,/,*,%)")

    if opr == '+':
        print("Result is :", num1+num2)
    elif opr == '-':
        print("Result is :", num1-num2)
    elif opr == '/':
        print("Result is :", num1/num2)
    elif opr == '%':
        print("Result is :", num1%num2)
    else:
         print("Invalid operation")

calculator()