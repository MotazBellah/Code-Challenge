def hexa_first_principles(hexadecimal):
    try:
        return int(hexadecimal, 16)
    except:
        return -1
