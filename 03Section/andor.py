marks1 = float(input("enter the marks of first test :"))
marks2 = float(input("enter the marks of first test :"))

absences =    float(input("enter the absences :"))
totalclass =  float(input("enter the total class conducted :"))
avg_marks = (marks1+marks2)/2
attendance = (totalclass - absences)/ totalclass

print("Avg marks :",round(avg_marks))
print("Attendance rate : ",round(attendance*100))

if(avg_marks >=6 and attendance >=0.8) :
        print("The student is forwarded to next grade")
elif(avg_marks <6 and attendance <0.8) :
        print("The student has failed due low avg marks and low attendance")
elif(attendance>0.8):
        print("The student has failed due  low marks")
else:
        print("The student has failed due  low attendance")
