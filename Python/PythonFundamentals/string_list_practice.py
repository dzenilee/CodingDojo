#Use only the built-in methods and functions from the previous tabs to do the following exercises. You might find a better way to do these tasks later on, but this is your chance to experiment with some built-in methods and functions so you can see how they work first-hand.

#Find and Replace
#In this string: str = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
str = "It's thanksgiving day. It's my birthday,too!"
print str.find('day')
print str.replace('day', 'month')

#Min and Max
#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First and Last
#Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[len(x)-1]
print first
print last

#New List
print [first, last]

#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
print len(x) #11

first_half = x[:len(x)/2]
second_half = x[len(x)/2:len(x)]
print first_half
print second_half

def print_each(lst1, lst2):
    new_arry = []
    new_arry.append(lst1)
    for each in lst2:
        new_arry.append(each)
    print new_arry

# print print_each(first_half, second_half) #[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

#Another way:
#list.insert(i, x): Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
second_half.insert(0,first_half) #inserts first_half to BEFORE index 0 of second_half
print second_half #[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
