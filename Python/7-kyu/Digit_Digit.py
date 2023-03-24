def square_digits(num):
    answer = ""
    for i in range(len(str(num))):
        answer += str(int(str(num)[i]) * int(str(num)[i]))
    return int(answer)
