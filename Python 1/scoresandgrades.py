import random

def scores(num):
    for i in range(0,num):
        grade = ""
        score = random.randrange(60,100)
        if score >= 90:
            grade = "A"
        elif score < 90 and score >= 80:
            grade = "B"
        elif score < 80 and score >= 70:
            grade = "C"
        else:
            grade = "D"
        print "Score:", score, "; Your grade is", grade
    print "End of the program. Bye!"

scores(10)
