import unittest

def get_max_money(x, y=[]):
    # Check if there are machines for sale
    if x[0] and y:
        # Use generator for better performance and efficient memory storage
        # (x[-1]+1 - i[0]) * i[-1]) => subtract total restructuring days
        # from the day of the machine has been bought and multiply the value by the machine's profit rate
        # add the value to (x[1] - i[i]), subtract the total money from machine price
        # performe this math operations if machine price less than the total money
        machine_gen = max((((x[-1]+1 - i[0]) * i[-1]) + (x[1]- i[1]) for i in y if x[1] >= i[1]), default=0)
        # Check if the machine makes more money than the total money
        # i.e check if buying a machine is worth it
        if machine_gen > x[1]:
            return machine_gen
        else:
            return x[1]
    else:
        return x[1]

x = [6 ,10 ,20]
y = [[6 ,12 ,1 ,3], [1, 9 ,1 ,2]
,[3 ,2 ,1, 2],
[8 ,20 ,5 ,4]
,[4 ,11, 7, 4]
,[2 ,10, 9, 1]]

print(get_max_money(x, y))
# get_max_money([6, 10, 20], [
#                             [6, 12, 1, 3],
#                             [1, 9, 1, 2],
#                             [3, 2, 1, 2],
#                             [8, 20, 5, 4],
#                             [4, 11, 7, 4],
#                             [2, 10, 9, 1]
#                             ]))

class TestGetMaxMoney(object):

    def test_case1(self):
        fun = get_max_money([6, 10, 20],
                            [[6, 12, 1, 3],
                             [1, 9, 1, 2],
                             [3, 2, 1, 2],
                             [8, 20, 5, 4],
                             [4, 11, 7, 4],
                             [2, 10, 9, 1]])
        print(fun)
        self.assertEqual(fun , 44)

if __name__ == '__main__':
    unittest.main()
