# Given an array of integers find the largest continuous sum

def large_cont_sum(arr):
    total = sum(arr)

    for i in range(1, len(arr)):
        x = sum(arr[:-i])
        if x > total:
            total = x

    return total

print(large_cont_sum([1,2,3]))
print(large_cont_sum([3,2,-3]))
print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
