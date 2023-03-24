def abbrev_name(name):
    answer = []
    for names in name.split():
        answer.append(names[0].upper())
    return '.'.join(answer)

# def abbrev_name(name):  # Another solution
#     names = name.split()
#     return names[0][0].upper() + "." + names[1][0].upper()
