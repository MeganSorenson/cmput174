# take in three grade inputs
grade1 = float(input("What is the first grade?"))
grade2 = float(input("What is the second grade?"))
grade3 = float(input("Whhat is the third grade?"))

# find highest value of these grades
if grade1 >= grade2 and grade1 >= grade3:
    highest = grade1
elif grade2 >= grade1 and grade2 >= grade3:
    highest = grade2
else:
    highest = grade3

# print highest grade
print("The highest grade is " + str(highest))
