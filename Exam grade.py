# Exam grading

grade = int(input("Enter exam score between 0 to 100:"))
if grade >= 0 and grade <= 39:
    print("fail")
elif grade >= 40 and grade <= 59:
    print("pass")

elif grade >= 40 and grade <= 59:
    print("pass")

elif grade >= 60 and grade <= 74:
    print("good")

elif grade >= 75 and grade <= 85:
    print("very good")

elif grade >= 85 and grade <= 100:
    print("excellent")

elif grade >= 100:
    print("Only values between 0 -100 are allowed")