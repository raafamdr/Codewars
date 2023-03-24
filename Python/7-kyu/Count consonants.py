def consonant_count(s):
    count = 0
    for letter in s.lower():
        if letter.isalpha() and letter not in 'aeiou':
            count += 1
    return count
