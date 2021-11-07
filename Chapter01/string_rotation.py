

def string_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1)>0:
        word = s2 + s2
        return s1 in word
    return False