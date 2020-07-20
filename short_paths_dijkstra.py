import heapq

def path_finder(maze):
    start = 0, 0
    maze_list = maze.split('\n')
    target = len(maze_list) - 1, len(maze_list[0]) - 1

    heap = []
    heapq.heappush(heap, (0, (start), None))
    explored = set()
    parent_dict = {}

    while len(heap):
        distance, node, parent = heapq.heappop(heap)

        if node == target:
            parent_dict[node] = parent
            c = 0
            while parent_dict[node]:
                node = parent_dict[node]
                c += 1
            return c

        if node not in explored:
            explored.add(node)
            parent_dict[node] = parent
        # print(node)
        for d, i in neighbors(maze_list, node, len(maze_list) - 1):
            if i not in explored:
                new_distance = distance + d
                add_or_replace(heap, (new_distance, i, node))

    return False


def neighbors(maze, node, n):
    x, y = node
    moves = [(x, y-1), (x, y+1),  (x-1, y), (x+1, y)]
    neighbors_node = set()

    for (r, c) in moves:
        # print(r, c)
        if 0 <= r <= n and 0 <= c <= n and maze[r][c] != 'W':
            d = r + c
            neighbors_node.add((d, (r,c)))

    return neighbors_node


def add_or_replace(heap, node):
    found = True
    for k, i in enumerate(heap):
        if i[1] == node[1]:
            found = False
            if node[0] < i[0]:
                heap[k] = node
                return heapq.heapify(heap)

    if found:
        heap.append(node)

    return heapq.heapify(heap)

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


print(shorest_path(a))
print(shorest_path(t))
print(shorest_path(b))
print(shorest_path(c))
print(shorest_path(d))
