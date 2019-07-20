def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None
    else:
        minimum = None
        maximum = None
        for i in ints:
            if minimum is None or minimum > ints[i]:
                minimum = ints[i]
            if maximum is None or maximum < ints[i]:
                maximum = ints[i]
        return minimum, maximum


def min_max_test(numbers, expected):
    actual = get_min_max(numbers)
    if actual == expected:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    min_max_test([4, 9, 0, 7, 1, 6, 2, 5, 3, 8], (0, 9))
    # Pass
    min_max_test([1, 1, 1, 1, 1], (1, 1))
    # Pass
    min_max_test([], (None, None))
    # Pass
