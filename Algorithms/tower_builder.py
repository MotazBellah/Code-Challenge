def tower_builder(n):
    tower = []
    count = 0
    for i in range(n):
        line = ' ' *(n-i-1)+ '*' + (count* '*') + ' ' *(n-i-1)
        count += 2
        tower.append(line)
    return tower
