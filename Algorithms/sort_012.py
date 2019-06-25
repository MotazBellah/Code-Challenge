def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    front_index = 0
    back_index = len(input_list) - 1
    while back_index:
        print(input_list)
        if input_list[front_index] > 1:
            input_list[front_index], input_list[front_index+1] = input_list[front_index+1], input_list[front_index]
            front_index += 1
            back_index -= 1
        elif input_list[back_index] < 1:
            input_list[back_index-1], input_list[back_index] = input_list[back_index], input_list[back_index-1]
            front_index += 1
            back_index -= 1
        else:
            front_index += 1
            back_index -= 1
            
        
    return input_list
