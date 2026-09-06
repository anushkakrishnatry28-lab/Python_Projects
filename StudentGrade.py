#Student Grade
marks=int(input("Enter the marks:- "))
if (marks>=90 and marks<=100):
    print("Grade A")
elif(marks>=75 and marks<90):
    print("Grade B")
elif(marks>=60 and marks<75):
    print("Grade C")
else:
    print("Fail")            
