#Given an array of strings, find strings that contain a certain character. If the string contains that character add the whole string to a array. When your program completes print the new array.

def find_char(lst, char):
    new_lst = []
    for word in lst:
        for letter in word:
            if letter == char:
                new_lst.append(word)
    print new_lst

l = ['hello','world','my','name','is','Anna']

find_char(l, 'o') #['hello','world']
