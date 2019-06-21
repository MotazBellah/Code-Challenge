# Problem 4

To test if a user belong to a group, we need to see if a user belongs to either the group directly,
or any descendants of the subgroup.  Testing all subgroups takes `O(g*u)` time where `g` is the
total number of groups and `u` is the average number of users per group.  Space requirements
are also `O(g * u)`.
