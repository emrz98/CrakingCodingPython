def string_compression(s: str) -> str:
    counter = 1
    last_letter = ""
    final_string = ""
    for letter in s:
        if letter == last_letter:
            counter +=1
        else:
            counter = 1
            final_string += last_letter + str(counter) 
            last_letter = letter

    if len(final_string) < len(s):
        return final_string
    return s
    pass

