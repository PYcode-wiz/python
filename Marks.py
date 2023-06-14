physics = int(input("Enter physics marks = "))
chemistry =int(input("Enter chemistry marks = "))
maths = int(input("Enter maths marks = "))
english = int(input("Enter maths marks = "))
nepali = int(input("Enter nepali marks = "))

if physics >= 32 and chemistry >= 32 and maths >= 32 and english >= 32 and nepali >= 32:
    total = physics + chemistry + maths + nepali + english
    per = total/5
    if per >= 80:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 40:
        grade = "C"
    else:
        grade = "F"

    print("The total = ",total)
    print("The percentage = ",per)
    print("The grade = ",grade)
else:
    print("You are fail.")