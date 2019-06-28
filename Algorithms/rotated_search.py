def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1

    while start_index <= end_index:
        
        mid_index = (start_index + end_index) // 2
        mid_value = input_list[mid_index]
        if mid_index < len(input_list) - 1:
            after_mid = input_list[mid_index + 1]
        before_mid = input_list[mid_index - 1]
        
        if number == mid_value:
            return mid_index
        
        elif mid_value > after_mid and mid_value > before_mid:
            if number > after_mid and number < before_mid:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1

        elif mid_value < before_mid:
            if number <= before_mid:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        
        elif number < mid_value:
            end_index = mid_index - 1
            
        else:
            start_index = mid_index + 1
        print(mid_value)
            
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
