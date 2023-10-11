marks=int(input("Enter Marks of Student in % : "))
if(marks<=100 and marks>90):
    print("Student Secured A+ grade")
elif(marks<=90 and marks>80):
    print("Student Secured A grade")
elif(marks<=80 and marks>70):
    print("Student Secured B+ grade")           
elif(marks<=70 and marks>60):
    print("Student Secured B grade")   
elif(marks<=60 and marks>50):
    print("Student Secured C+ grade")
elif(marks<=50 and marks>40):
    print("Student Secured C grade")
elif(marks<=40 and marks>35):
    print("Student Secured Pass grade")
elif(marks<35 and marks>=0):
    print("Student Secured Fail grade")    
else:
    print("Please Enter Correct Marks ")     
     