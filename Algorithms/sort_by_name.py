# Sort these integers for me ...
#
# By name ...
#
# Do it now !
#
# Input
# Range is 0-999
#
# There may be duplicates
#
# The array may be empty
#
# Example
# Input: 1, 2, 3, 4
# Equivalent names: "one", "two", "three", "four"
# Sorted by name: "four", "one", "three", "two"
# Output: 4, 1, 3, 2
# Notes
# Don't fret about formatting rules. If rules are consistently applied it has no effect anyway:
# e.g. one hundred one, one hundred two is same order as one hundred and one, one hundred and two
# e.g. ninety eight, ninety nine is same order as ninety-eight, ninety-nine

def sort_by_name(arr):
    #  sort the Input array based on the key`convert function`
    return sorted(arr, key=convert)

def convert(a):
    if not a:
        return "zero"
    d = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    r = []
    if a // 100:
        r.append("{} hundred".format(d[a // 100]))
    if a % 100:
        if a % 100 <= 20:
            r.append(d[a % 100])
        else:
            b = d[a % 100 // 10 * 10]
            if a % 10: b += " {}".format(d[a % 10])
            r.append(b)
    return " ".join(r)
