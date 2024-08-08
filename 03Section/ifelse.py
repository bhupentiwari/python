marks1 = float(input("enter the marks of first test :"))
marks2 = float(input("enter the marks of first test :"))

absences =    float(input("enter the absences :"))
totalclass =  float(input("enter the total class conducted :"))
avg_marks = (marks1+marks2)/2
attendance = (totalclass - absences)/ totalclass

print("Avg marks :",round(avg_marks))
print("Attendance rate : ",round(attendance*100))

if(avg_marks >=6) :
    if(attendance >=0.8) :
        print("The student is forwarded to next grade")
    else:
        print("The student has failed")
else:
    print("The student has failed")
    
