def pluralize(singular_arr):
    plural_arr = []
    vowel = ["a", "i", "u"]
    coronal = ["s", "r"]
    for singular in singular_arr:
        if singular[-2:] == "ie":
            if len(singular) >= 3 and singular[-3] in coronal:
                plural_arr.append(singular+"En")
            else:
                plural_arr.append(singular+"n")
        if singular[-1:] in vowel:
            plural_arr.append(singular+"'s")
        else:
            plural_arr.append(singular+"s")
    print plural_arr

singular_arr = ["berie", "kasie", "karie", "sona", "soni", "sonu", "sonou", "sone"]
pluralize(singular_arr)
