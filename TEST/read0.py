from max_money import get_max_money
import itertools


with open('input.txt') as f:
    x = f.read().splitlines()
z = (i.split() for i in x if len(i.split())==3)
v = (i.split() for i in x if len(i.split())!=3)
length = sum(1 for i in x if len(i.split())==3)

test = {}

s = 0
e = 0

for i in range(length):
    # print(x)
    x = next(z)
    y = []
    if int(x[0]):
        e += int(x[0])
        v, y_backup = itertools.tee(v)
        y = itertools.islice(y_backup, s, e)
        s = e
    print(get_max_money(x, y))
