def missing_element(arr1, arr2):
    return set(arr1) - set(arr2)


def missing_element(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return i

print(missing_element([1,2,3,4,5,6], [3,7,2,1,4,6]))
