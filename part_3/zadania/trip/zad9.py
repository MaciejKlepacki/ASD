from zad9testy import runtests
from math import inf

def trip(M):
    pass


def gen_adjacency_list(M):
    G = [[] for _ in range(len(M) * len(M)[0]]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j-1] and M[i][j-i]
            G[i*len(M[0])+j] = 


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )


def dfs_list(graph):
    n = len(graph)
    visited = [False] * n
    parent = [None] * n
    discovery = [0] * n
    processed = [0] * n
    time = 0

    def dfs_visit(v):
        nonlocal time
        visited[v] = True
        time += 1
        discovery[v] = time
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                dfs_visit(u)
        time += 1
        processed[v] = time

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return visited, parent, discovery, processed

if __name__ == "__main__":
    graph_list = [
        [1, 4],
        [2],
        [3],
        [],
        [2]
    ]
