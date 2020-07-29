# You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions
# (i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1].
# Number of climb rounds between adjacent locations is defined as difference of location altitudes (ascending or descending).

# Location altitude is defined as an integer number (0-9).

from  heapq import *

def path_finder(area):
    start = 0, 0
    maze = area.split('\n')
    target = len(maze) - 1, len(maze[0]) - 1

    stack = []
    stack.append((0, start))

    explored = set()

    while stack:
        distance, node = heappop(stack)

        if node == target:
            return distance

        if node not in explored:
            explored.add(node)


        for d, i in neighbors(maze, node, len(maze)-1):
            # print(i, d)
            if i not in stack and i not in explored:
                heappush(stack, (d+distance, i))

    return False


def neighbors(maze, node, n):
    x, y = node
    current_value = maze[x][y]
    moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    neighbors_node = set()

    for (r, c) in moves:
        if 0 <= r <= n  and 0 <= c <= n:
            d = abs(int(current_value) - int (maze[r][c]))
            neighbors_node.add((d, (r, c)))

    return neighbors_node


# def traverse(parent, target):
#     total = 0
#     while True:
#         vertex, value = parent[target]
#         # print(vertex)
#         if vertex:
#             target = vertex
#         else:
#             break
#         total += value
#
#     yield total

# Solution 2

MOVES = ((1,0), (-1,0), (0,1), (0,-1))

def path_finder2(area):
    area = list(map(list,area.splitlines()))
    x_max, y_max = len(area), len(area[0])
    end = x_max - 1, y_max - 1
    queue = [(0,(0,0))] # total cost, pos

    while len(queue):
        c, (x, y) = heappop(queue)
        if (x,y)==end:
            return c
        if area[x][y].isdigit():
            val = int(area[x][y])
            area[x][y] = 'X'
            for dx, dy in MOVES:
                i, j = pos = x+dx, y+dy
                if 0 <= i < x_max and 0 <= j < y_max and area[i][j].isdigit():
                    edge = abs(val - int(area[i][j]))
                    heappush(queue,(c+edge,pos))


a = "\n".join([
  "000",
  "000",
  "000"
])

b = "\n".join([
  "010",
  "010",
  "010"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

d = "\n".join([
  "0707",
  "7070",
  "0707",
  "7070"
])

e = "\n".join([
  "700000",
  "077770",
  "077770",
  "077770",
  "077770",
  "000007"
])

f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])

print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))
print(path_finder(e))
print(path_finder(f))
print(path_finder(g))
