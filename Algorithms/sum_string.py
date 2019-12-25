import re
def sum_from_string(string):
    n = re.findall(r'[\d]+', string)
    return sum([int(i) for i in list(n)])
    
