def isUnique(word):
    word_set = set(word)
    return len(word_set) == len(word)

def isUniqueTwoFors(word):
    for i in range(len(word) - 1):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                return False
    
    return True

def isUniqueVector(word):
    arreglo = [0] * 1000
    for c in word:
        arreglo[ord(c)] += 1

    for i in arreglo:
        if i > 1: return False
    return True