parent = {}
rank = {}

########################
#UNION & FIND definition
########################
def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
########################

def kruskal_alg(graph, e):
    result = False                      #boolean value, set to True if the given edge belongs to any MST.
    minimum_spanning_tree = set()
    for vertex in graph['vertices']:
        make_set(vertex)                #at the beginning, each vertex is in a different SET.
    edges = list(graph['edges'])
    edges.sort()
    weights = []
    for edge in edges:
        weights.append(edge[0])
        
    #this is to put the given edge first among the othe edges with the same weigth.
    edges[edges.index(e)] = edges[weights.index(e[0])]
    edges[weights.index(e[0])] = e
    #print(edges)
    ###
    
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):          #if the SET of the two vertices are different, it means that I'm discovering a new edge, so I add it to MST.
            if e == edge:                           #check if the current edge is equal to given edge.
                result = True
            union(vertex1, vertex2)                 #now that the edge will be added to MST, the two vertices will be part of the same SET.
            minimum_spanning_tree.add(edge)
	    
    if result:
        print("\nThe MST found is: ")
        return sorted(minimum_spanning_tree)
    else:
        return "It doesn't exist any MST which contains the given edge e"

graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': set([
(7, 'A', 'B'),
(5, 'A', 'D'),
(7, 'B', 'A'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(7, 'B', 'E'),
(8, 'C', 'B'),
(5, 'C', 'E'),
(5, 'D', 'A'),
(9, 'D', 'B'),
(7, 'D', 'E'),
(6, 'D', 'F'),
(7, 'E', 'B'),
(5, 'E', 'C'),
(15, 'E', 'D'),
(8, 'E', 'F'),
(9, 'E', 'G'),
(6, 'F', 'D'),
(8, 'F', 'E'),
(11, 'F', 'G'),
(9, 'G', 'E'),
(11, 'G', 'F'),
])
}

print(kruskal_alg(graph, (11, 'F', 'G')))
print()
print(kruskal_alg(graph, (7, 'B', 'E')))
