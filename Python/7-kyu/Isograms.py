def is_isogram(string):
    answer = ""

    for letter in string.lower():
        if letter in answer:
            return False

        answer += letter
    return True
