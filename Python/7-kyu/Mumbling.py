def accum(s):
    s = s.lower()
    answer = ""
    for i in range(len(s)):
        for j in range(i+1):
            if j == 0:
                answer += s[i].upper()
            else:
                answer += s[i]
        answer += "-"

    return answer[:-1]

# Another solution
# def accum(s):
#     i = 0
#     answer = ""
#     for letter in s:
#         answer += letter.upper() + letter.lower() * i + "-"
#         i += 1

#     return answer[:-1]
