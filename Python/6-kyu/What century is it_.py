def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

def what_century(year):
    year = century(int(year))

    if year % 10 == 1 and year != 11:
        return str(year) + "st"
    elif year % 10 == 2 and year != 12:
        return str(year) + "nd"
    elif year % 10 == 3 and year != 13:
        return str(year) + "rd"
    else:
        return str(year) + "th"
