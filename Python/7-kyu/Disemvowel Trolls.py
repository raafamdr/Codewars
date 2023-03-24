def disemvowel(string_):
    answer = ""
    for i in range(len(string_)):
        if string_[i] not in 'aeiouAEIOU':
            answer += string_[i]
    return answer

# Another solution
# def disemvowel(string_):
#     for letter in 'aeiouAEIOU':
#         string_ = string_.replace(letter, '')
#     return string_

# Another solution using replace
# def disemvowel(string_):
#     answer = string_
#     for i in range(len(string_)):
#         if string_[i] in 'aeiouAEIOU':
#             answer = answer.replace(string_[i], "")
#     return answer
