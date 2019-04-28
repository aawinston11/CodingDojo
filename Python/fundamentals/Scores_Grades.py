import random

def scores():
    print "Scores and Grades"
    for i in range(10):
        score = random.randint(60, 100)
        print "Score: " + str(score) + "; " + "Your grade is " + grade(score)
    print "End of the program. Bye!"

def grade(num):
    if num>=60 and num<=69:
        return "D"
    elif num>=70 and num<=79:
        return "C"
    elif num>=80 and num<=89:
        return "B"
    elif num>=90 and num<=100:
        return "A"

scores()        