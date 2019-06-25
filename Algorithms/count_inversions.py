def count_inversions(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    print(left, right)

    # Call mergesort recursively with the left and right half
    left = count_inversions(left)
    right = count_inversions(right)

    # Merge our two halves and return
    return merge(left, right)

def merge(left, right):
    '''
    Given two ordered lists, merge them together in order,
    returning the merged list. '''
    merged = []
    count = 0
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
            count += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    merged += left[left_index:]
    merged += right[right_index:]
    print(count)
    return merged, count


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
t = [7, 5, 3, 1]
#print('{} to {}'.format(test_list_1, count_inversions(test_list_1)))
#print('{} to {}'.format(test_list_2, count_inversions(test_list_2)))
#print('{} to {}'.format(test_list_3, count_inversions(test_list_3)))
print(count_inversions(t))
    
