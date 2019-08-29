def find_start(trips):
    '''function to find out what is the starting place of the journey
    input: list of trips with start and distenation
    output: string starting place'''

    start = set()
    dist = set()
    for trip in trips:
        start.add(trip[0])
        dist.add(trip[1])
    return list(start - dist)[0]
