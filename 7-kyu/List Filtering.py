def filter_list(l):
    answer = []
    for element in l:
        if not isinstance(element, str):
            answer.append(element)
    return answer
