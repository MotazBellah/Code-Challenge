def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    old_array = array
    while len(old_array) > 2:
        half_index = int(len(old_array) / 2)
        half_value = old_array[half_index]
        print(half_value)
        print(old_array)
        if half_value == target:
            return array.index(target)
        elif half_value < target:
            new_array = old_array[half_index:]
            old_array = new_array
        else:
            new_array = old_array[:half_index]
            old_array = new_array

    return -1


def binary_search_method2(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division in Python 3

        mid_element = array[mid_index]

        if target == mid_element:                       # we have found the element
            return mid_index

        elif target < mid_element:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half

        else:                                           # the target is greater than mid element
            start_index = mid_element + 1               # we will search only in the right half

    return -1

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)
