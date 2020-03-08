# Write a program that will convert a hexadecimal number
# represented as a string (e.g. "10af8c"), to its decimal equivalent.
#
# The program should return -1 for invalid hexadecimal strings.

def hexa_first_principles(hexadecimal):
    try:
        return int(hexadecimal, 16)
    except:
        return -1
