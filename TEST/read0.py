from max_money import get_max_money
import itertools



with open('input.txt') as f:
    x = f.read().splitlines()
z = (i.split() for i in x if len(i.split())==3)
v = (i.split() for i in x if len(i.split())!=3)
length = sum(1 for i in x if len(i.split())==3)

test = {}
# z = (i for i in y if len(i) == 3)
# v = (i for i in y if len(i) != 3)

# print(list(z))
# print(list(v))



# print(len(z))
# print('==============')
# print(len(v))
s = 0
e = 0
# length = sum(1 for _ in z)
for i in range(length):
    # print(x)
    x = next(z)
    y = []
    if int(x[0]):
        e += int(x[0])
        # print(s, e)
        # y = v[s:e]
        v, y_backup = itertools.tee(v)
        y = itertools.islice(y_backup, s, e)
        # print(list(y))
        s = e
        # print(y)
        # for j in range(int(x[0])):
        #     y.append(v.pop(j))
            # print(v.pop(j))
    print(get_max_money(x, y))
    # print('==============')
    # print(x)
    # print(y)
# p = 1
# case1 = {}
# for i in z:
#
#     m = []
#     if int(i[0]):
#         print(i)
#         for k in range(int(i[0])):
#             m.append(v[k])
#         print(i)
#         case1['x'] = i
#         case1['y'] = m
#         test['case'+str(p)] = case1
#     else:
#         case1['x'] = i
#         case1['y'] = m
#         test['case1'] = case1
#     p += 1

# print(test)
