import re
def isAnagram(test, original):
    a = test.lower()
    b = original.lower()
    return sorted("".join(re.findall(r'[a-z0-9]+',a)))== sorted("".join(re.findall(r'[a-z0-9]+',b)))
