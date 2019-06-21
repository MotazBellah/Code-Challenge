In this problem, I have implemented the recursion for finding the element. At each recursive step I have implemented following:
First I have checked the name of the group whether it is same as the user I am looking for then I checked in the users list of that group. Then I went for its child groups.
If at any point I find the user. I returned True but aafter checking all the groups and users, if I don't find the user. Then I returned

Time complexity: O(depth x no. of users)
Space complexity: O(depth x no. of users)
