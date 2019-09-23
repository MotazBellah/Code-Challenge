#!/usr/bin/env python3
import unittest
import itertools
from max_money import get_max_money

def read_input():
    """Read the input file
    output: tuble (the info about the restructuring
    and info about single machine and the length of restructuring data)"""
    # Use with to make sure the file will be closed after the block executed
    with open('input.txt') as f:
        # Split the line at line breaks
        x = f.read().splitlines()
    # Get the data of restructuring, three positive integers N , C , and D
    # Use generator expression for time and space efficiency
    restructuring_info = (i.split() for i in x if len(i.split())==3)
    # Get the data of single machine, four integers D, P, R and G
    machine_info = (i.split() for i in x if len(i.split())!=3)
    # Get the length of restructuring data
    length = sum(1 for i in x if len(i.split())==3)

    return restructuring_info, machine_info, length


def test_inputs():
    """Take the data from the input file
    and display the max money by calling
    the get_max_money function and return generator"""
    # Get data from the input file and unpacking it to three variable
    get_data = read_input()
    restructuring_info = get_data[0]
    machine_info = get_data[1]
    length = get_data[2]
    # start, end to slice the generator
    start, end = 0, 0
    # Loop through lenght of restructuring
    # Get x (restructuring_info) and y (machine_info)
    # Use x, y as a parameter for get_max_money function
    for i in range(length):
        x = next(restructuring_info)
        y = []
        # Check if there a machine
        # clone the machine_info generator to slice it
        # the cliced generator represent the machine informations
        # that related to restructuring_info
        if int(x[0]):
            end += int(x[0])
            machine_info, m_backup = itertools.tee(machine_info)
            y = itertools.islice(m_backup, start, end)
            start = end

        yield ('Case ' +str(i+1) + ": " + str(get_max_money(x, y)))



# Unit test suite
class TestGetMaxMoney(unittest.TestCase):

    def test_case1(self):
        fun = get_max_money([6 ,10 ,20],[[6 ,12 ,1 ,3],
                                         [1, 9 ,1 ,2],
                                         [3 ,2 ,1, 2],
                                         [8 ,20 ,5 ,4],
                                         [4 ,11, 7, 4],
                                         [2 ,10, 9, 1]])
        self.assertEqual(fun , 44)

    def test_case2(self):
        fun = get_max_money([0 ,11 ,30])
        self.assertEqual(fun , 11)

    def test_case3(self):
        fun = get_max_money([1 ,12 ,30], [[30 ,10 ,5 ,3]])
        self.assertEqual(fun , 12)

    def test_case4(self):
        fun = get_max_money([1 ,10 ,2], [[1 ,10 ,2 ,1]])
        self.assertEqual(fun , 10)

    def test_case5(self):
        fun = get_max_money([2 ,10 ,11], [[1 ,10 ,4 ,3],
                                          [1 ,10 ,9 ,3]])
        self.assertEqual(fun , 33)

    def test_case6(self):
        fun = get_max_money([0,0,0])
        self.assertEqual(fun , 0)


if __name__ == '__main__':
    tests = test_inputs()
    print("========================================")
    print("Test Cases Results Are The Following: ")

    for test in tests:
        print(test)

    unittest.main() # unittest runner
