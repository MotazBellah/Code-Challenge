def countTinyPairs(a, b, k):
    count = 0
    b = b[::-1]
    for i in range(len(a)):
        y = str(a[i]) + str(b[i])
        if int(y) < k:
            count += 1

    return count


a =  [1, 2, 3]
b= [1, 2, 3]
k=  31

print(countTinyPairs(a, b, k))
