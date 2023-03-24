def xo(s):
    i = j = 0
    for letter in s:
        if letter in 'oO':
            i += 1
        elif letter in 'xX':
            j += 1
    return True if i == j else False # same as return i == j

# Another solution
# def xo(s):
#     return s.lower().count('o') == s.lower().count('x')
