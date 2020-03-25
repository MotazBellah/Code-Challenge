# Given a string in form 'AABBBCC' compress it to became 'A2B3C2'

def compress_string(some_str):
    count = 1
    total = some_str[0]

    for i in some_str[1:]:
        if i == total[-1]:
            count += 1
        else:
            total += str(count)
            count = 1
            total += i
    return total + str(count)

print(compress_string('A'))
print(compress_string('AAAABBBBEEEERRRTGHY'))
print(compress_string('AAAABBBBEEEERRAARTGHY'))
