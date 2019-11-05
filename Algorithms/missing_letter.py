def find_missing_letter(chars):
    x = [ord(i) for i in chars]
    y = [i for i in range(ord(chars[0]), ord(chars[0]) + len(chars) + 1)]
    missi = set(y).difference(x)
    return chr(list(missi)[0])
