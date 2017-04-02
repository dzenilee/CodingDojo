import random
# random_num = random.random() #will return a floating point number, that is 0.0 <= random_num < 1.0
# random_num = random.randint(60, 100) #will return integer


# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

def score_grade():
    print "Scores and Grades"
    for ea in range(0, 10):
        random_num = random.randint(60, 100)
        if random_num < 69:
            grade = 'D'
        elif random_num < 79:
            grade = 'C'
        elif random_num < 89:
            grade = 'B'
        else:
            grade = 'A'
        print "Score: {}; Your grade is {}".format(random_num, grade)

score_grade()
