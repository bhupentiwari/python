employee = {"name":"Bhupendra","employeecode":"1112","doj":"11-09-2019"}
key = input("What information you required for employee: ")
print("then entered information required is: ",key)
result = employee.get(key.lower(),"information does not exist ")
print("the result is",result)