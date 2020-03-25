# Determine if the string has a uniqe characters

def uniqe_char2(s):
    output = ''
    for i in s:
        if i in output:
            return False
        output += i

    return True

def uniqe_char(s):
    return len(s) == len(set(s))

print(uniqe_char('abcde'))
print(uniqe_char('aabcde'))
