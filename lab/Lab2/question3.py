# take in grade input
grade = float(input("Input the grade:"))

# evaluate for categorization
if grade > 4 or grade < 0:
    category = "Invalid!"
elif grade < 1:
    category = "Failure!"
elif grade < 1.3:
    category = "Poor!"
elif grade < 2.3:
    category = "Satisfactory!"
elif grade < 3.3:
    category = "Good!"
else:
    category = "Excellent!"

# print category message
print("The grade is " + category)
