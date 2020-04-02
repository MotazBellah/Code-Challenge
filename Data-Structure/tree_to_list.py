# representation of a Tree using a list of lists.
def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBrach):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBrach, t, []])
    else:
        root.insert(1, [newBrach, []])

    return root

def insertRight(root, newBrach):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBrach, [], t])
    else:
        root.insert(2, [newBrach, []])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)

print(r)
