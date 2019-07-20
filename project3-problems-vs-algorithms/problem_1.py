def sqrt(n):
    """
    Finds the square root of a number.
    :param n: the number to find the square root of
    :return: the integer floored square root.  Example sqrt(16) = 4, sqrt(21)=4, sqrt(27)=5
    """
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        mid_plus_one_squared = (mid + 1) * (mid + 1)
        if mid_squared <= n < mid_plus_one_squared:
            return int(mid)
        elif mid_squared < n:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == '__main__':
    print(sqrt(27))
    # 5

    print(sqrt(21))
    # 4

    print(sqrt(16))
    # 4

    print(sqrt(2.5))
    # 1

    print(sqrt(1))
    # 1

    print(sqrt(0))
    # 0

    print(sqrt(0.5))
    # 0

    print(sqrt(-1))
    # None
