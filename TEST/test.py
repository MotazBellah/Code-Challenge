import unittest
from max_money import get_max_money

# test cases value
TEST_CASE = {'Case1': {'x': [6 ,10 ,20],
                      'y': [[6 ,12 ,1 ,3],
                            [1, 9 ,1 ,2],
                            [3 ,2 ,1, 2],
                            [8 ,20 ,5 ,4],
                            [4 ,11, 7, 4],
                            [2 ,10, 9, 1]]
                      },
             'Case2': {'x': [0 ,11 ,30],
                      'y': []
                      },
             'Case3': {'x': [1 ,12 ,30],
                       'y': [[30 ,10 ,5 ,3]]
                      },
             'Case4': {'x': [1 ,10 ,2],
                       'y': [[1 ,10 ,2 ,1]]
                      },
             'Case5': {'x': [2 ,10 ,11],
                       'y': [[1 ,10 ,4 ,3],
                             [1 ,10 ,9 ,3]]
                      },
             'Case6': {'x': [0 ,0 ,0],
                       'y': []
                       }
            }

# display the output value
print('Case 1: {}'.format(get_max_money(TEST_CASE['Case1']['x'], TEST_CASE['Case1']['y'])))
print('Case 2: {}'.format(get_max_money(TEST_CASE['Case2']['x'], TEST_CASE['Case2']['y'])))
print('Case 3: {}'.format(get_max_money(TEST_CASE['Case3']['x'], TEST_CASE['Case3']['y'])))
print('Case 4: {}'.format(get_max_money(TEST_CASE['Case4']['x'], TEST_CASE['Case4']['y'])))
print('Case 5: {}'.format(get_max_money(TEST_CASE['Case5']['x'], TEST_CASE['Case5']['y'])))
print('Case 6: {}'.format(get_max_money(TEST_CASE['Case6']['x'], TEST_CASE['Case6']['y'])))


class TestGetMaxMoney(object):
    
    def test_case1(self):
        fun = get_max_money(TEST_CASE['Case1']['x'], TEST_CASE['Case1']['y'])
        self.assertEqual(fun , 44)

    def test_case2(self):
        fun = get_max_money(TEST_CASE['Case2']['x'], TEST_CASE['Case2']['y'])
        self.assertEqual(fun , 11)

    def test_case3(self):
        fun = get_max_money(TEST_CASE['Case3']['x'], TEST_CASE['Case3']['y'])
        self.assertEqual(fun , 12)

    def test_case4(self):
        fun = get_max_money(TEST_CASE['Case4']['x'], TEST_CASE['Case4']['y'])
        self.assertEqual(fun , 10)

    def test_case5(self):
        fun = get_max_money(TEST_CASE['Case5']['x'], TEST_CASE['Case5']['y'])
        self.assertEqual(fun , 33)

    def test_case6(self):
        fun = get_max_money(TEST_CASE['Case6']['x'], TEST_CASE['Case6']['y'])
        self.assertEqual(fun , 0)


if __name__ == '__main__':
    unittest.main()
