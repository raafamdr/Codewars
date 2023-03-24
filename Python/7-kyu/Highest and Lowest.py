def high_and_low(numbers):
    array = []

    for number in numbers.split():
        array.append(int(number))

    answer = f'{max(array)} {min(array)}'
    return answer
