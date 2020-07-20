def heap_add_or_replace(heap, triplet):
    for k, i in enumerate(heap):
        if i[0] == triplet[0]:
            if triplet[1] < i[1]:
                heap[k] = triplet
                return heap.sort(key= lambda i: i[1])

    heap.append(triplet)

    # print(heap)
    heap.sort(key= lambda i: i[1])
    return heap



x = list()
heap_add_or_replace(x, ((2,3), 0.9, (1,0)))
# print(str(x))

(heap_add_or_replace(x, ((7,2), 0.3, (2,2))))
print(heap_add_or_replace(x, ((7,2), 0.2, (2,6))))
print(x)

# print(heap_add_or_replace([1,25,3,7,2]))
def t(heap, triplet):
    for k, i in enumerate(heap):
        if i[0] == triplet[0]:
            print('k')
            if triplet[1] < i[1]:
                heap[k] = triplet


    return heap


print(t([(1,2,3), (3,4,5)], (1,1,4)))
