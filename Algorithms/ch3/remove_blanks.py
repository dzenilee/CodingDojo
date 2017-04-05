# Create a function that, given a string, returns all of that string's contents but without blanks.

#declare a function with a name

#test case for input that we assign to a variable

#parse through the string and find all the characters that are blanks

def remove_blanks(text):
    new_string = ""
    for char in text:
        if char != " ":
            new_string += char
    print new_string

remove_blanks("I love coding!")
