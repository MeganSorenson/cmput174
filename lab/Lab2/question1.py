# takes two grade inputs
grade1 = float(input("What is the first grade?"))
grade2 = float(input("What is the second grade?"))

# check whether grades are equal or not and prints message
if grade1 == grade2:
    check_equal = "equal!"
else:
    check_equal = "NOT equal!"

print(str(grade1) + " and " + str(grade2) + " are " + check_equal)
