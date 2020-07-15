def path_finder(maze):
    start = (0, 0)
    maze_list = maze.split('\n')
    target = len(maze_list) -1, len(maze_list[0]) -1

    stack = []
    stack.append(start)
    explored = set()

    while len(stack):
        node = stack.pop(0)
        if node == target:
            return True

        explored.add(node)

        for n in neighbors(node, maze, len(maze_list) -1):
            if n not in stack and n not in explored:
                stack.append(n)

    return False

def neighbors(vertex, graph, n):
    walls = get_walls(graph)
    maze_list = graph.split('\n')
    x, y = vertex
    moves = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    neighbors_node = set()
    for (r, c) in moves:
        print(r,c)
        if 0 <= r <= n and 0 <= c <= n:
            print(maze_list[r][c])
        if 0 <= r <= n and 0 <= c <= n and (r, c) not in walls:
            neighbors_node.add((r,c))

    return neighbors_node


def get_walls(maze):
    maze = maze.split('\n')
    walls = set()
    for i in range(len(maze)):
        if 'W' in maze[i]:
            # for j in range(len(maze[1])):
            #     if maze[i][j] == 'W':
            j = maze[i].find('W')
            walls.add((i, j))

    return walls


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


# print(a)
# print('===========')
# print(a.split('\n'))


print(path_finder(a))
# print(path_finder(b))
# print(path_finder(c))
# print(path_finder(d))
