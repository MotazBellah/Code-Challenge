# Write a method that takes an array of consecutive (increasing) letters as
# input and that returns the missing letter in the array.

# You will always get an valid array.
# And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

def find_missing_letter(chars):
    # get the unicode code for each letter in the list
    x = [ord(i) for i in chars]
    # create a list of number from unicode code of 1st letter to last letter
    y = [i for i in range(ord(chars[0]), ord(chars[0]) + len(chars) + 1)]
    # use set and difference method to get the missing number (unicode code)
    missi = set(y).difference(x)
    # convert unicode code to unicode character and return it
    return chr(list(missi)[0])
