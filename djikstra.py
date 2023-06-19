def genGraph(paths, size):
    graph = [[0 for i in range(size)] for j in range(size)]
    for i in paths:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]
    return graph

def main():
    size = 9
    paths = [
        [0, 1, 8],
        [0, 2, 13],
        [0, 3, 14],
        [1, 2, 7],
        [1, 6, 14],
        [2, 3, 6],
        [2, 7, 20],
        [2, 4, 8],
        [5, 4, 6],
        [5, 6, 5],
        [6, 8, 6],
        [5, 7, 12],
        [8, 7, 7]
    ]
    graph = genGraph(paths, size)
    startingNode = 2
    visitedNodes = [startingNode]
    notVisitedNodes = []
    distances = []
    paths = []
    for i in range(size):
        if i != startingNode:
            notVisitedNodes.append(i)
            distances.append(-1)
            paths.append([])
            continue
        distances.append(0)
        paths.append([i])
    while len(notVisitedNodes) > 0:                                 #Se repete até todos os nodes serem fechados
        for currentNode in visitedNodes:                            #Passa por cada um dos nodes já fechados pra checar os próximos caminhos
            for currentNotVisited in notVisitedNodes:               #Passa por cada um dos nods ainda não fechados pra ver se há caminho
                if graph[currentNode][currentNotVisited] == 0:      #Se for 0 não há um caminho para ir
                    continue
                calculatedDistance = graph[currentNode][currentNotVisited] + distances[currentNode]
                print(paths)
                newPath = paths[currentNode] + [currentNotVisited]
                print(f'Path from {currentNode} to {currentNotVisited} with distance of {calculatedDistance}')
                if (distances[currentNotVisited] == -1) or (distances[currentNotVisited] > calculatedDistance):
                    distances[currentNotVisited] = calculatedDistance
                    paths[currentNotVisited] = newPath
        toClose = [-1, -1]
        for currentNotVisited in notVisitedNodes:
            if distances[currentNotVisited] == -1:
                continue
            if toClose[0] == -1:
                toClose = [currentNotVisited, distances[currentNotVisited]]
            if toClose[1] > distances[currentNotVisited]:
                toClose = [currentNotVisited, distances[currentNotVisited]]
        print(f'Closed the node {toClose[0]} with distance of {toClose[1]}')
        visitedNodes.append(toClose[0])
        notVisitedNodes.remove(toClose[0])
        #for currentNotVisited in notVisitedNodes:
        #    distances[currentNotVisited] = -1
        print()
    print(f'Best distances: {distances}')
    print()
    for i in range(size):
        print(f'Best path for the node {i}: {paths[i]}')

main()
