def find_smallest_int(arr):
    smaller = 9999
    for i in arr:
        if i < smaller:
            smaller = i
    return smaller
    # return min(arr) # more effective
