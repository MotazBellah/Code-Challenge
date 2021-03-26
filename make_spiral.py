# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python
# Your task, is to create a NxN spiral with a given size.
# For example, spiral with size 5 should look like this:
# 00000
# ....0
# 000.0
# 0...0
# 00000
# Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

# Because of the edge-cases for tiny spirals, the size will be at least 5.

# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

def spiralize(size):
    if size <= 0:
        return []

    core = [ [[1,1,1,1], [0,0,0,1], [1,0,0,1], [1,1,1,1]], [[1]], [[1,1],[0,1]], [[1,1,1],[0,0,1],[1,1,1]] ][size%4]

    while len(core) < size:
        for x in [0,1]:
            core.insert(0, [ x for i in core[0] ] )
            core.append([ x for i in core[0] ])
            for line in core:
                line.insert(0, x)
                line.append(x)
            core[1][0] = int(not x)

    return core
