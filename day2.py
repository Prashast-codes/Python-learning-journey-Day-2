# today is my day two of learning python and yeah todays topics are :

# CONDITIONAL STATE [IF,ELSE,ELIF]:
# 1. IF : it checks first codition , Elif : checks additional condition , Else : checks leftover conditions.

age = int(input("please enter your age :"))
if age >=18:
    print("you are eligible for vote")

# Challenge :
1.
marks = int(input("please enter your marks:"))
if marks >=(40) :
    print("Pass")

2. # with else:

Age = int(input("Enter your age :"))
if Age >= (18) :
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

# 3. Grading system by python :

Marks = int(input("Enter your marks:"))
if Marks >= 90 :
    print("Grade : A+")
elif Marks >= 70:
    print("Grade : B")
elif Marks >= 60 :
    print("Grade : C")
elif Marks < 40 :
    print("Better luck next time")  
else :
    print("Pass")

# 4. Electricity usage checkerc:

Units = int(input("Please enter your unit of electricity :"))
if Units >= 300 :
    print("High Usage")
elif Units >= 200 :
    print("Moderate Usage")
elif Units >= 100 :
    print("Low Usage")
else :
    print("Very low usage")
