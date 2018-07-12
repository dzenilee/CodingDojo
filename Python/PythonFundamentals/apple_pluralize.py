def pluralize(singular_arr):
    plural_arr = []
    coronal = ["s", "r"]
    for singular in singular_arr:
        if singular[-2:] == "ie":
            if singular[-3] in coronal:
                plural_arr.append(singular+"En")
            else:
                plural_arr.append(singular+"n")
        else:
            if singular[-1] in ["a", "i", "u"] and singular[-2:] != "ou":
                plural_arr.append(singular+"'s")
            else:
                plural_arr.append(singular+"s")
    print plural_arr

singular_arr = ["berie", "kasie", "karie", "sona", "soni", "sonu", "sonou", "sone"]
pluralize(singular_arr)

# output = ['berieEn', 'beries', 'kasieEn', 'kasies', 'karieEn', 'karies', "sona's", "soni's", "sonu's", "sonou's", 'sones']
