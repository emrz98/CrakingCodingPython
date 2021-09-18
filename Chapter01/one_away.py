

def one_away(str1, str2):

    remove = abs (len(str1) - len(str2))
    if remove > 1: return False

    

    if len(str1) == len(str2):
        cont = 0
        for i in range (len(str1)):
            if str1[i] != str2[i]:
                cont += 1
        return cont <= 1

    min_str = str1 if len(str1) < len(str2) else str2
    max_str = str1 if len(str1) > len(str2) else str2
    cont = 0
    shift = 0
    for i in range (len(min_str)):
        if (min_str[i] != max_str[i + shift]):
            if shift == 1:
                return False
            shift = 1
    return False if min_str[-1] != max_str[len(min_str) -1 + shift] else True
