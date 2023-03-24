def descending_order(num):
    answer = sorted(str(num), reverse=True)
    answer = ''.join(answer)
    return int(answer)
