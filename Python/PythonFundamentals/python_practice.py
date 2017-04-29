# Wed 4/5/17 Python Week 1 Lecture 3

superheros = {
    "quickster": "The Flash",
    "buster": "The Hulk",
    "flyer": "silver surfer",
    "detective": "Bat Man",
}

# print superheros # {'detective': 'Bat Man', 'flyer': 'silver surfer', 'quickster': 'The Flash', 'buster': 'The Hulk'}
# print superheros['quickster'] # The Flash

for hero in superheros:
    print "The key is", hero
    print "The value for", hero, "is", superheros[hero] # prints the values
# The key is detective
# The value for detective is Bat Man
# The key is flyer
# The value for flyer is silver surfer
# The key is quickster
# The value for quickster is The Flash
# The key is buster
# The value for buster is The Hulk

for go in superheros.itervalues():
    print go
# Bat Man
# silver surfer
# The Flash
# The Hulk

for fish in superheros.iterkeys():
    print fish
# detective
# flyer
# quickster
# buster

for fish, go in superheros.items():
    print fish, go
# detective Bat Man
# flyer silver surfer
# quickster The Flash
# buster The Hulk

print superheros.items() # returns list of tuples
# [('detective', 'Bat Man'), ('flyer', 'silver surfer'), ('quickster', 'The Flash'), ('buster', 'The Hulk')]

for hero in superheros.items(): # returns each key-value tuple
    print hero
# ('detective', 'Bat Man')
# ('flyer', 'silver surfer')
# ('quickster', 'The Flash')
# ('buster', 'The Hulk')

more_superheros = {
    "quickster": ["The Flash", "Quick Silver"],
    "buster": ["The Hulk", "The Thing"],
    "flyer": ["silver surfer", "Iron Man", "Superman"],
    "detective": ["Bat Man", "The Owl"],
}

for hero_type, heros in more_superheros.items():
    print hero_type
    for hero in heros:
        print "  *", hero
# detective
#   * Bat Man
#   * The Owl
# flyer
#   * silver surfer
#   * Iron Man
#   * Superman
# quickster
#   * The Flash
#   * Quick Silver
# buster
#   * The Hulk
#   * The Thing

for hero_type in more_superheros.iterkeys():
    print hero_type
    for hero in more_superheros[hero_type]:
        print "  *", hero
# detective
#   * Bat Man
#   * The Owl
# flyer
#   * silver surfer
#   * Iron Man
#   * Superman
# quickster
#   * The Flash
#   * Quick Silver
# buster
#   * The Hulk
#   * The Thing

hero_string = "silver surfer Iron Man Superman surfers"
print hero_string.find("surfer") #7 (index 0 of the first instance of that string)
print hero_string.find("surfers") #32
print hero_string.find("serfer") #-1 (when it can't find the string)
