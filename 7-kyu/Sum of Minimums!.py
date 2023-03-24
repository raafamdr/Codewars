def sum_of_minimums(numbers):
    minimums = []
    for i in range(len(numbers)):
        minimums.append(min(numbers[i]))
    return sum(minimums)
