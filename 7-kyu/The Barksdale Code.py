def decode(strng):
    decode_string = ""
    for number in strng:
        if number == '0':
            decode_string += '5'
        elif number == '5':
            decode_string += '0'
        else:
            decode_string += str(10-int(number))
    return decode_string
