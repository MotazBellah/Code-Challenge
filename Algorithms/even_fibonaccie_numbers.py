# https://projecteuler.net/problem=2
def fibonaccie(n):
    x, y = 1, 1
    s = []
    while x <= n:
        x, y = x + y, x
        if y % 2 == 0:
            s.append(y)



    return sum(s)

print fibonaccie(4000000)
