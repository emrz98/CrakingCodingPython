def urlLyfy(word, length):
    start = 0
    for i in range(len(word)):
        if word[i] != " ":
            start = i
            break

    newString = ""
    for i in range(start, start + length):
        if word[i] == " ":
            newString += "%20"
        else:
            newString += word[i]
    return newString