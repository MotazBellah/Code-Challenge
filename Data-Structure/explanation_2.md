I have written a recursive function for this question which takes input the suffix, path and the list of required files which are found till now. Each time I find a file ending with .c will be appended to this file.

Run time complexity: O(depth X Avg. number of directory in each level)

Space complexity: O(depth)
