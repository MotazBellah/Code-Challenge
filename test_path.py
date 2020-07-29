def path_finder(area):
    start = 0, 0
    maze = area.split('\n')
    target = len(maze) - 1, len(maze[0]) - 1

    stack = []
    stack.append((start, None, 0))

    explored = set()
    parent_dict = {}
    total = 0
    while stack:
        node, parent, distance = stack.pop(0)

        if node == target:
            parent_dict[node] = (parent, distance)
            while True:
                vertex, value = parent_dict[node]
                if vertex:
                    node = vertex
                else:
                    break
                total += value
                # print(node, value)
            break

        if node not in explored:
            explored.add(node)
            parent_dict[node] = (parent, distance)
            # total += distance

        for i, d in neighbors(maze, node, len(maze)-1):
            # print(i, d)
            if i not in stack and i not in explored:
                stack.append((i, node, d))
        stack.sort(key=lambda i: i[2])


    return total


def neighbors(maze, node, n):
    x, y = node
    current_value = maze[x][y]
    moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    neighbors_node = set()

    for (r, c) in moves:
        if 0 <= r <= n  and 0 <= c <= n:
            d = abs(int(current_value) - int (maze[r][c]))
            neighbors_node.add(((r, c), d))

    return neighbors_node
