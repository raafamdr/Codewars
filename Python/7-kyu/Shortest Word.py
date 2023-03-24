def find_short(s):
    s = s.split()
    short = len(s[0])
    for word in s:
        if len(word) < short:
            short = len(word)
    return short

# def find_short(s):
#     return len(min(s.split(), key=len))  # Another way to solve
