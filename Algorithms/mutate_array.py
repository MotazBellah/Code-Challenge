def mutateTheArray(n, a):
    b = []
    a.insert(0,0)
    a.append(0)

    for k in range(1, n+1):
        x = a[k-1] + a[k] + a[k+1]
        b.append(x)

    return b


a = [4, 0, 1, -2, 3]
print(mutateTheArray(5, a))
