def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    def swap(j, k):
        x = a[j]
        a[j] = a[k]
        a[k] = x

    a = input_list.copy()
    p0 = 0
    p2 = len(a) - 1
    i = 0
    while i <= p2:
        if a[i] == 0:
            swap(p0, i)
            p0 += 1
            if i < p0:
                i = p0
        elif a[i] == 1:
            i += 1
        else:  # a[i] == 2
            swap(p2, i)
            p2 -= 1

    return a


def sort_012_test(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    sort_012_test([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    # [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
    # Pass

    sort_012_test([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # Pass

    sort_012_test([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    # [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    # Pass

    sort_012_test([])
    # []
    # Pass

    sort_012_test([0, 0, 0])
    # [0, 0, 0]
    # Pass

    sort_012_test([1, 1, 1])
    # [1, 1, 1]
    # Pass

    sort_012_test([2, 2, 2])
    # [2, 2, 2]
    # Pass

    sort_012_test([2, 1, 0])
    # [0, 1, 2]
    # Pass
