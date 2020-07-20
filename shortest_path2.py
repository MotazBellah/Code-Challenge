# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
# (i.e. North, East, South, West). Return the minimal number of steps to exit position [N-1, N-1]
# if it is possible to reach the exit from the starting position.
# Otherwise, return false in JavaScript/Python and -1 in C++/C#/Java.

# Empty positions are marked .. Walls are marked W.
def path_finder(maze):
    # initial vertex
    start = (0, 0)
    # Convert to list and get the maze size
    maze_list = maze.split('\n')
    # Target n-1, n-1
    target = len(maze_list) -1, len(maze_list[0]) -1
    # Create queue FIFO DS
    stack = []
    # Add initial vertex, distance to initial vertex, parent
    stack.append((start, 0, None))
    # Create explored set, to trace the explored vertices
    explored = set()
    parent_dict = {}
    # Loop till the stack is empty
    while len(stack):
        # Unpack the first element in the queue
        node, d, parent = stack.pop(0)
        # If node reachs to the target
        if node == target:
            parent_dict[node] = parent
            # Call traverse function to get the path from initial vertex to the target
            tt = traverse(parent_dict, target)
            return next(tt)
        # If not not in explored
        #  Add it to explored, and update the parent dict
        if node not in explored:
            explored.add(node)
            parent_dict[node] = parent

        # stack.extend(((n, v, node) for n, v in neighbors(node, maze_list, len(maze_list) -1, target) if (n, v) not in stack and (n) not in explored))
        # get the neighbors and update the queue
        for n, v in neighbors(node, maze_list, len(maze_list) -1, target):
            if (n, v, node) not in stack and (n) not in explored:
                stack.append((n, v, node))
        stack.sort( key=lambda i: i[1])

    return False


def neighbors(vertex, graph, n, target):
    # Unpack the initial vertex, current vertex, and the target
    g, h = 0, 0
    x, y = vertex
    a, b = target
    # All possible moves
    moves = [(x, y-1), (x, y+1),  (x-1, y), (x+1, y)]
    neighbors_node = set()
    # Loop througth the moves
    # Get all the neighbors nodes to the current node
    for (r, c) in moves:
        if 0 <= r <= n and 0 <= c <= n and graph[r][c] != 'W':
            # Get the distance from the node (r, c) to the target
            d = (a - r) + (b - c)
            # Get the distance from the node (r, c) to the initial vertex
            k = (r - g) + (c - h)
            neighbors_node.add(((r,c), (k+d)))
        # print(neighbors_node)

    return neighbors_node

def traverse(parent, target):
    # Create counter
    l = 0
    # Update the counter, while the node has a parent
    # i.e increase the counter, till reach to the root
    while True:
        node = parent[target]
        if node:
            target = node
        else:
            break
        l += 1
    yield l




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

print(path_finder(a))
print(path_finder(t))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))
