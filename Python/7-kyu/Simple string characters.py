def solve(s):
    uppercase_counter = lowercase_counter = numbers_counter = special_counter = 0
    for char in s:
        if char.isupper():
            uppercase_counter += 1
        elif char.islower():
            lowercase_counter += 1
        elif char.isnumeric():
            numbers_counter += 1
        elif not char.isalpha():
            special_counter += 1
    return [uppercase_counter, lowercase_counter, numbers_counter, special_counter]
