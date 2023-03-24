def validate_pin(pin):
    size = len(pin)

    if pin.isnumeric():
        if size == 4 or size == 6:
            return True
        else:
            return False
    else:
        return False
