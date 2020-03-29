# Reverse string with Recursion
# Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.
def reverse(s, output=''):
    if s and len(s) != len(output):
        i = len(output) + 1
        output += s[-i]
        return reverse(s, output)
    else:
        return output


print(reverse('hello world'))
print(reverse('abcdef ghiA'))


def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    return our_string[::-1]
