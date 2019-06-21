As I have to design a data structure for a Least Recently Used (LRU) cache with O(1) operations. It's the best option to go with dictionary in python which has constant time access of values with particular key.
To keep track of the order of the values I have created a queue with the help of python deque, which allows constant time popleft().

Get Time complexity: O(1)
Set Time complexity: O(1)

Space complexity of the LRU: O(capacity)
