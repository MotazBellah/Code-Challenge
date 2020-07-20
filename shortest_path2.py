# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
# (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

# Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.

def path_finder(maze):
    start = (0, 0)
    maze_list = maze.split('\n')
    target = len(maze_list) -1, len(maze_list[0]) -1

    stack = []
    stack.append((start, 0, None))

    explored = set()
    parent_dict = {}
    while len(stack):
        node, d, parent = stack.pop(0)
        if node == target:
            parent_dict[node] = parent
            tt = traverse(parent_dict, target)
            return next(tt)

        if node not in explored:
            explored.add(node)
            parent_dict[node] = parent

        # stack.extend(((n, v, node) for n, v in neighbors(node, maze_list, len(maze_list) -1, target) if (n, v) not in stack and (n) not in explored))
        for n, v in neighbors(node, maze_list, len(maze_list) -1, target):
            if (n, v) not in stack and (n) not in explored:
                stack.append((n, v, node))
        stack = sorted(stack, key=lambda i: i[1])

    return False


def neighbors(vertex, graph, n, target):
    g, h = 0, 0
    x, y = vertex
    a, b = target

    moves = [(x, y-1), (x, y+1),  (x-1, y), (x+1, y)]
    neighbors_node = set()
    for (r, c) in moves:
        if 0 <= r <= n and 0 <= c <= n and graph[r][c] != 'W':
            d = (a - r) + (b - c)
            # k = (r - g) + (c - h)
            neighbors_node.add(((r,c), (d)))
        # print(neighbors_node)

    return neighbors_node


# def create_graph(maze):
#     start = (0, 0)
#     maze_list = maze.split('\n')
#     target = len(maze_list) -1, len(maze_list[0]) -1




a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

t = "\n".join([
  "...",
  "...",
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


# print(a)
# print('===========')
# print(a.split('\n'))

aa = {(0, 0): None, (1, 0): (0, 0), (0, 1): (0, 0), (1, 1): (1, 0), (2, 0): (1, 0), (0, 2): (0, 1), (2, 1): (1, 1), (1, 2): (1, 1), (2, 2): (2, 1)}
def traverse(parent, target):
    l = 0
    while True:
        node = parent[target]
        if node:
            target = node
        else:
            break
        l += 1
    yield l

# print(traverse(aa, (2,2)))
print(path_finder(a))
print(path_finder(t))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))
