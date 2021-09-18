def string_compression(s: str) -> str:
    counter = 1
    last_letter = "" + s[0]
    final_string = ""
    for letter in s[1:]:
        if last_letter != letter:
            final_string += last_letter + str(counter)
            last_letter = letter
            counter = 1
        else:
            counter += 1

    final_string += last_letter + str(counter)
    if len(final_string) < len(s):
        return final_string
    return s
    pass

