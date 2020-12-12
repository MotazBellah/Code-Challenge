def containsCloseNums(nums, k):
    d = {}

    for i, v in enumerate(nums):
        if v in d:
            if (i - d[v][-1]) <= k:
                return True

            d[v].append(i)
        else:
            d[v] = [i]
    return False

nums = [0, 1, 2, 3, 5, 2]
k = 2

print(containsCloseNums(nums, k))
