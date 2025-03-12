#assign_grade(score)

def grades():
    grade = int(input("Please enter your grade:"))
    if grade < 0 or grade > 100:
        print("Invalid score! Enter a value between 0 and 100")
    elif grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    elif grade >= 60:
        print("Grade: D")
    elif grade >= 0:
        print("Grade: F")
        
grades()

while True:
    a = input("Run again?:")
    if a == "yes":
        grades()
        
    else:
        b = print("Program done.")
        break
    