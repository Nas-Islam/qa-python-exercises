def gradeCalc():
    print("Welcome to the Grade Calculator!")
    mathsmark = int(input("Please enter your maths mark: "))
    chemmark = int(input("Please enter your chemistry mark: "))
    physicsmark = int(input("Please enter your physics mark: "))

    percentage = (mathsmark + chemmark + physicsmark) / 3
    if percentage >= 70:
        grade = 'You scored a grade of: A'
    elif percentage >= 60:
        grade = 'You scored a grade of: B'
    elif percentage >= 50:
        grade = 'You scored a grade of: C'
    elif percentage >= 40:
        grade = 'You scored a grade of: D'
    else:
        grade = 'You failed.'
    print(percentage,"%")
    print(grade)


gradeCalc()
