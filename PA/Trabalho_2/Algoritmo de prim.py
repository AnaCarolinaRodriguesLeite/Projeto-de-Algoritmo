import heapq

def prim(graph, start):
    # Inicializa as estruturas de dados
    visited = set()
    heap = [(0, start)]
    mst = {}

    while heap:
        # Obtém o menor peso da heap
        (weight, vertex) = heapq.heappop(heap)

        # Verifica se o vértice já foi visitado
        if vertex in visited:
            continue

        # Marca o vértice como visitado e adiciona a aresta na MST
        visited.add(vertex)
        if vertex != start:
            mst[vertex] = weight

        # Adiciona na heap os vizinhos do vértice atual
        for neighbor, neighbor_weight in graph[vertex].items():
            if neighbor not in visited:
                heapq.heappush(heap, (neighbor_weight, neighbor))

    return mst

n, m = map(int, input().split())

graph = {i: {} for i in range(1, n+1)}

for i in range(1, m+1):
    u, v, w = map(int, input().split())

    # Adiciona a aresta no grafo
    graph[u][v] = w
    graph[v][u] = w

    # Calcula a MST sem a aresta (u, v)
    mst = prim(graph, 1)
    # Obtém o peso da MST sem a aresta (u, v)
    weight_without_edge = sum(mst.values())

    # Remove a aresta (v, u) do grafo
    del graph[u][v]
    del graph[v][u]

    # Calcula a MST com a aresta (u, v)
    mst = prim(graph, 1)
    # Obtém o peso da MST com a aresta (u, v)
    weight_with_edge = sum(mst.values()) + w

    # Imprime o peso mínimo da MST que contém a aresta (u, v)
    print(min(weight_with_edge, weight_without_edge))
