import sys

infinit = sys.maxsize

#-----------------------------------------
graph = [[0, 5, 3, 0],
         [5, 0, 2, 0],
         [3, 2, 0, 4],
         [0, 0, 4, 0]]


nodes = []
n = len(graph)

#-----------------------------------------

nodes = [infinit] * n

#-----------------------------------------
start = int(input('start: '))
nodes[start] = 0

#-----------------------------------------
visited = [False] * n

#-----------------------------------------
def get_min_node(nodes, visited):
    min_value = infinit
    min_index = -1
    for i in range(n):
        if nodes[i] < min_value and not visited[i]:
            min_value = nodes[i]
            min_index = i
    return min_index
    
#-----------------------------------------

def dijkstra(graph, start):
    for j in range(n):
        u = get_min_node(nodes, visited)
        visited[u] = True

        for v in range(n):
            if (not visited[v]) and (graph[u][v] != 0):
                if nodes[u] + graph[u][v] < nodes[v]:
                    nodes[v] = nodes[u] + graph[u][v]

#-----------------------------------------
dijkstra(graph, start)

#-----------------------------------------
for i in range(n):
    print("to node", i, "is", nodes[i])



