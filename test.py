#!/usr/bin/env python3
import unittest
import itertools
from max_money import get_max_money

def read_input():
    """Read the input file
    output: tuble (the info about the restructuring
    and info about single machine and the length of restructuring data)"""
    # Use with to make sure the file will be closed after the block executed
    with open('snapshot_input.txt') as f:
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


if __name__ == '__main__':
    tests = test_inputs()
    print("========================================")
    print("Test Cases Results Are The Following: ")

    for test in tests:
        print(test)
