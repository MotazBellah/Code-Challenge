def pair_sum(arr, target):
    pair = set()
    for i in range(1, len(arr)):
        if sum([arr[i-1], arr[i]]) == target:
            pair.add((arr[i-1], arr[i]))

    return pair


print(pair_sum([1,3,2,2], 4))
