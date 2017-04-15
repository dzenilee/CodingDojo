#Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

# Use the python built-in round function to convert that floating point number into an integer
x = .23945593
y = .798839238
x_rounded = round(x) # x_rounded will be rounded down to 0
y_rounded = round(y) # y_rounded will be rounded up to 1

print x_rounded
print y_rounded

import random

def coin_tosses():
    tail_count = 0
    head_count = 0
    for ea in range(0,1000):
        random_num = random.random()
        rounded = round(random_num)
        if rounded == 0:
            toss = 'tail'
            tail_count += 1
        else:
            toss = 'head'
            head_count += 1
        print 'Attemp #{}: Throwing a coin... It\'s a {}! ... Got {} head(s) so far and {} tail(s) so far'.format(ea, toss, head_count, tail_count)

coin_tosses()
