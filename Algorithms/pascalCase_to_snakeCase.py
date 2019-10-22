import string

def to_underscore(s):
    # Make sure the input is a string
    if str(s) in string.digits:
        return str(s)
    s = s[0].lower() + s[1:]
    new = list(s)
    u = [i for i in new if i.isupper()]
    for i in u:
        n = new.index(i)
        new.insert(n, '_')

    return "".join(new).lower()
