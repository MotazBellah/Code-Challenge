def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    """
    sorted_string = sort_string(string)
    count_lower, count_upper = 0, 0
    string_list = []
    for letter in string:
        if letter == letter.lower():
            string_list.append(sorted_string[1][count_lower])
            count_lower += 1
        else:
            string_list.append(sorted_string[0][count_upper])
            count_upper += 1

    return ''.join(string_list)
    

def sort_string(string):
    list_string = list(string)
    start = len(string) - 1
    while start:
        for letter in range(1, len(string)):
            prev_letter, current_letter = list_string[letter-1], list_string[letter]

            if ord(prev_letter) > ord(current_letter):
                list_string[letter-1], list_string[letter] = current_letter, prev_letter
        start -= 1

    upper_list = [i for i in list_string if i == i.upper()]
    lower_list = [i for i in list_string if i == i.lower()]
    return upper_list, lower_list
