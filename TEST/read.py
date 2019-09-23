from max_money import get_max_money
import fileinput

for line in fileinput.input(files=('input.txt')):
    print(line)

with open('input.txt') as f:
    x = f.read().splitlines()
y = [i.split() for i in x]

test = {}
z = [i for i in y if len(i) == 3]
v = [i for i in y if len(i) != 3]



# print(len(z))
# print('==============')
# print(len(v))
s = 0
e = 0
for i in range(len(z)):
    x = z[i]
    y = []
    if int(x[0]):
        e += int(x[0])
        # print(s, e)
        y = v[s:e]
        s = e
        # print(y)
        # for j in range(int(x[0])):
        #     y.append(v.pop(j))
            # print(v.pop(j))
    # print(get_max_money(x, y))
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
