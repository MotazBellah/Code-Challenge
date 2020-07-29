from operator import itemgetter

def heap_add_or_replace(heap, triplet):
    found = True
    for k, i in enumerate(heap):
        if i[0] == triplet[0]:
            found = False
            if triplet[1] < i[1]:
                heap[k] = triplet
                return heap.sort(key= lambda i: i[1])

    if found:
        heap.append(triplet)

    # print(heap)
    heap.sort(key= lambda i: i[1])
    return heap


def neighbors(maze_graph, vertex):
    x, y = vertex
    moves = [(x, y-1), (x, y+1),  (x-1, y), (x+1, y)]
    neighbors_node = set()

    for i in moves:
        if i in maze_graph[vertex].keys():
            neighbors_node.add(i)
        # print(neighbors_node)

    return neighbors_node

def Dijkstra(maze_graph,initial_vertex):
    # Variable storing the exploredled vertices vertexes not to go there again
    explored_vertices = list()

    # Stack of vertexes
    heap = list()

    #Parent dictionary
    parent_dict = dict()
    # Distances dictionary
    distances = dict()

    # First call
    initial_vertex = (initial_vertex, 0, initial_vertex)#vertex to visit, distance from origin, parent
    heap_add_or_replace(heap,initial_vertex)
    while len(heap) > 0:
        # get the triplet (vertex, distance, parent) with the smallest distance from heap list using heap_pop function.
        vertex, distance, parent = heap.pop(0)
        # if the vertex of the triplet is not explored:
        if vertex not in explored_vertices:
        #     map the vertex to its corresponding parent
            parent_dict[vertex] = parent
            explored_vertices.append(vertex)
            distances[vertex] = distance


            for i in neighbors(maze_graph, vertex):
                if i not in explored_vertices:
                    d = distance + maze_graph[vertex][i]
                    heap_add_or_replace(heap, (i, d, vertex))

    return explored_vertices, parent_dict, distances


maze_graph = {
    (0,0): {(1,0):3,(0,1):5},
    (1,0): {(0,1):1,(1,1):2},
    (0,1): {(1,1):1,(0,2):2},
    (1,1): {(1,2):2},
    (0,2): {(1,2):4},
    (1,2): {(0,1):3},
    (2,2): {(1,2):2,(3,2):1},
    (2,1): {(1,1):3,(2,2):7},
    (3,2): {(2,1):2}
    }

explored_vertices, parent_dict, distances = Dijkstra(maze_graph, (0,0))
print(distances)
print("explored vertices order: {}".format(explored_vertices))

for vertex, parent in sorted(parent_dict.items(), key=itemgetter(1, 0)):
    print("Vertex {}is reached from veretex {}, and its distance from initial vertex is {}".format(vertex,parent,distances[vertex]))
