def get_middle(s):
    if len(s) % 2 == 0:
        return f'{s[int(len(s)/2) - 1]}{s[int(len(s)/2)]}'
    else:
        return s[int(len(s)/2)]
