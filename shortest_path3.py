# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
# (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

# Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.

def path_finder(maze):
    start = (0, 0)
    maze_list = maze.split('\n')
    target = len(maze_list) -1, len(maze_list[0]) -1

    stack = set()
    stack.add((start, None))
    explored = set()
    parent_dict = {}
    while len(stack):
        node, parent = stack.pop()
        if node == target:
            parent_dict[node] = parent
            c = 0
            while parent_dict[node]:
                c += 1
                node = parent_dict[node]
            return c

        explored.add(node)
        parent_dict[node] = parent

        for n in neighbors(node, maze_list, len(maze_list) -1):
            if n not in explored:
                stack.add((n, node))

    return False

def neighbors(vertex, graph, n):
    x, y = vertex
    moves = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    neighbors_node = set()
    for (r, c) in moves:
        if 0 <= r <= n and 0 <= c <= n and graph[r][c] != 'W':
            neighbors_node.add((r,c))

    return neighbors_node



a = "\n".join([
  ".W.",
  ".W.",
  "..."
])


b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

t = "\n".join([
  "...",
  "...",
  "..."
])


# print(a)
# print('===========')
# print(a.split('\n'))


print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))
print(path_finder(t))
