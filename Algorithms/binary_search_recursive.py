def binary_search(array, target):

    return binary_search_recursive(array, target, 0, len(array) - 1)

def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start_index > end_index:
        return -1


    mid_index = (start_index + end_index)//2

    mid_element = array[mid_index]

    if target == mid_element:
        return mid_index

    elif target < mid_element:
        return binary_search_recursive(array, target, start_index, mid_index - 1)                   # we will only search in the left half
    else:
        return binary_search_recursive(array, target, mid_index + 1, end_index)
