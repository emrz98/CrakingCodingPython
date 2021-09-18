def palindromePermutation(string):
    string = string.replace(" ", "").lower()
    lenght_word = len(string)
    dict_char = {}
    for i in string:
        if i in dict_char.keys():
            dict_char[i] += 1
        else:
            dict_char[i] = 1 
    if lenght_word%2 == 0:
        for key, value in dict_char.items():
            if value % 2 == 1:
                return False
        return True
    else:
        alone = False
        for key, value in dict_char.items():
            if value % 2 == 1:
                if alone:
                    return False
                alone = True
        return True