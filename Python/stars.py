#PART 1
#Create a function called draw_stars() that takes a list of numbers and prints out *.
def draw_stars(lst):
    for ea in lst:
        print ea * '*'

x = [4, 6, 1, 3, 5, 7, 25]

draw_stars(x)

#PART 2
#Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
def draw_stars_ii(lst):
    for ea in lst:
        if isinstance(ea, int):
            print ea * '*'
        else:
            print ea[0].lower() * len(ea)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars_ii(x)
