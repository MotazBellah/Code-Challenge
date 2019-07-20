def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       :param input_list: Input array to search and the target
       :param number: number to find
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(input_list) - 1
    while left <= right:
        if input_list[left] < input_list[right]:
            # Case 1: we have a sorted list, do binary search
            mid = (left + right) // 2
            if input_list[mid] == number:
                return mid
            if number < input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Case 2: we have a rotated list.
            # If a[r] < n < a[l] our number isn't in the list, return -1
            if input_list[right] < number < input_list[left]:
                return -1
            # Create a midpoint.  At least one half will be ordered.
            mid = (left + right) // 2
            if input_list[mid] == number:
                return mid
            # If the left half is ordered and the number is within its range, do binary search on the left half
            if input_list[left] <= number <= input_list[mid - 1]:
                right = mid - 1
            else:
                # Otherwise, Search the right half.
                left = mid + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def is_ok(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    is_ok([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    # Pass

    is_ok([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    # Pass

    is_ok([[6, 7, 8, 1, 2, 3, 4], 8])
    # Pass

    is_ok([[6, 7, 8, 1, 2, 3, 4], 1])
    # Pass

    is_ok([[6, 7, 8, 1, 2, 3, 4], 10])
    # Pass

    is_ok([[], 10])
    # Pass
