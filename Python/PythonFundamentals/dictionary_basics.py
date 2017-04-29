#Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

my_dict = {"name": "Jenny", "age": "30", "country of birth": "Korea", "favorite langauge": "Python"}

def about_me():
    for key in my_dict.keys():
        print "My", key, "is", my_dict[key]

about_me()
