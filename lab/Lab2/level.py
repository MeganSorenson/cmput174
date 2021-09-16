# Student Level Categorization Tool for a Self-Paced Online Course
# categorizes students based on two quiz marks

# get both quiz mark inputs as floating points
quiz1 = float(input("Enter marks for quiz 1 >"))
quiz2 = float(input("Enter marks for quiz 2 >"))

# evaluate which level student is assigned
#   level 3: >= 80 on both quizzes
#   level 2: >= 50 on both quizes
#   redo low quiz: <50 on one quiz and >= 50 on one quiz
#   level 1: <50 on both quizzes
if quiz1 >= 80 and quiz2 >= 80:
    level = "Level 3"
elif quiz1 >= 50:
    if quiz2 >= 50:
        level = "Level 2"
    else:
        level = "Redo quiz2"
elif quiz2 >= 50:
    if quiz1 < 50:
        level = "Redo quiz1"
else:
    level = "Level 1"

# print category assigned based on quiz marks
print(level)
