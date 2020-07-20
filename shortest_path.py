def path_finder(maze):
    start = (0, 0)
    maze_list = maze.split('\n')
    target = len(maze_list)-1, len(maze_list[0])-1


    # stack.append(start)
    stack = add_or_replace([], start, 0)
    explored = set()
    # print(stack)
    #
    while len(stack):
        # print('c')
        # node = stack.pop(0)
        node, distance = remove(stack)
        # print(explored)
        if node == target:
            return True

        explored.add(node)
        # print(stack)

        for v, d in neighbors(node, maze_list, len(maze_list)-1, target):

                # print(v, d)
            if v not in explored:
                print(v)
                new_distance = distance + d
                # if (v, new_distance) not in stack:
                stack = add_or_replace(stack, v, new_distance)


    return False


def neighbors(vertex, graph, n, target):
    x, y = vertex
    t = str(target[0]) + str(target[1])

    moves = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    neighbors_node = set()
    for (r, c) in moves:
        if 0 <= r <= n and 0 <= c <= n and graph[r][c] != 'W':

            v = str(r) + str(c)
            d = int(t) - int(v)
            neighbors_node.add(((r,c), d))
    # print(vertex, neighbors_node)

    return neighbors_node

def add_or_replace(min_heap, vertex, distance):
    # print('j')
    if min_heap:
        min_heap_dict = dict((y, x) for y, x in min_heap)
    else:
        # print('h')
        min_heap_dict = dict(min_heap)

    if vertex in min_heap_dict:
        if min_heap_dict[vertex] > distance:
            min_heap_dict[vertex] = distance
        else:
            pass
    else:
        min_heap_dict[vertex] = distance
    # print(min_heap_dict)
    x = sorted(min_heap_dict.items(), key= lambda i: i[1])
    # print(x)

    return x

def remove(min_heap):
    return min_heap.pop(0)


a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

# print(path_finder(a))

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])
# print(path_finder(b))
c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])
print(path_finder(c))

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


# print(path_finder(a))
# print(path_finder(b))
# print(path_finder(c))
# print(path_finder(d))
