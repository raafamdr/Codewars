def consecutive(arr, a, b):
    for i in range(len(arr)):
        if arr[i] == a:
            return arr[i+1] == b
        elif arr[i] == b:
            return arr[i + 1] == a

# Another solution
def consecutive(arr, a, b):
    return abs(arr.index(a) - arr.index(b)) == 1
