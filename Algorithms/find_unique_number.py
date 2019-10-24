def find_uniq(arr):
    # your code here
    set_list = set(arr)
    for i in set_list:
        if arr.count(i) == 1:
            return i
