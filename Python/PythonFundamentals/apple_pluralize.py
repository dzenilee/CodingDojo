def pluralize(singular_arr):
    plural_arr = []
    vowel = ["a", "i", "u", "e"]
    coronal = ["s", "r"]
    for singular in singular_arr:
        if singular[-1:] in vowel: # for all vowel-final singular forms,
            if singular[-2:] == "ie": # if singular form ends in -ie,
                if singular[-3] in coronal: # and it's preceded by a coronal,
                    plural_arr.append(singular+"En") # -sieEn or -rieEn
                else:
                    plural_arr.append(singular+"n") # -ien
            else: # if singular form does not end in -ie,
                if singular[-1:] != "e" and singular[-2:] != "ou": # and it doesn't end in -e or -ou,
                    plural_arr.append(singular+"'s") # -a's, -i's, -u's
                else:
                    plural_arr.append(singular+"s") # -es, -ous
    print plural_arr

singular_arr = ["berie", "kasie", "karie", "sona", "soni", "sonu", "sonou", "sone"]
pluralize(singular_arr)

# output = ['berieEn', 'kasieEn', 'karieEn', "sona's", "soni's", "sonu's", 'sonous', 'sones']
