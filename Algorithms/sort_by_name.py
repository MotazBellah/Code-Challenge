def sort_by_name(arr):
    return sorted(arr, key=convert)

def convert(a):
    if not a: return "zero"
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
