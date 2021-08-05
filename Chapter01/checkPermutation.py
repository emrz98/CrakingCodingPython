def checkPermutation(words):
    word1_sorted = "".join(sorted(words[0]))
    word2_sorted = "".join(sorted(words[1]))
    if(word1_sorted == word2_sorted):
        return True
    return False