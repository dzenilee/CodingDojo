# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
  zipped = zip(arr1, arr2) # list of key-value tuples
  return dict(zipped) # list to dictionary

# harder way
def make_dict2(arr1, arr2):
    new_dict = {}
    for key in arr1:
        key_index = arr1.index(key) # stores the index of arr1's key
        new_dict[key] = arr2[key_index]
    return new_dict

print name.index('Eli') #1
print make_dict2(name, favorite_animal) #{'Eli': 'cat', 'Shane': 'dolphins', 'Brendan': 'giraffe', 'Amy': 'ticks', 'Pariece': 'spider', 'Oscar': 'llamas', 'Anna': 'horse'}
