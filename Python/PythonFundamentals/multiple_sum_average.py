#Multiples:
#Part I
#Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for num in range(1,1001):
    if num % 2 != 0:
        print num

#Part II
#Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for num in range(5,1000000):
    if num % 5 == 0:
        print num

#Sum List
#Create a program that prints the sum of all the values in the list:
a = [1, 2, 5, 10, 255, 3]
print sum(a) #276

#Average List
#Create a program that prints the average of the values in the list:
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a) #46
print float(sum(a))/len(a) #46.0
