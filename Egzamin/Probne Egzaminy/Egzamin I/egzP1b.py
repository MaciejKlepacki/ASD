from itertools import count
from pydoc import parentname

from debugpy.common.timestamp import current
from gpxpy.geo import distance
from jupyter_core.version import parts

from egzP1btesty import runtests
from queue import PriorityQueue
inf = float('inf')

def turysta( G, D, L ):

    G = edge_list_to_adjacency_list(G)
    distances = dijkstra(G, D, L)



    return distances[L]




def edge_list_to_adjacency_list(G):
    num_nodes = max(max(u,v) for u, v, _ in G) + 1
    T = [[] for _ in range(num_nodes)]

    for u, v, w in G:
        T[u].append((v, w))
        T[v].append((u, w))
    return T

def dijkstra(G, D, L):
    n = len(G)
    distances = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    counter = [inf for _ in range(n)]
    distances[D] = 0
    counter[D] = 0

    PQ = PriorityQueue()
    PQ.put((0,D))

    while not PQ.empty():
        current_distance, vertex = PQ.get()

        if current_distance > distances[vertex]: continue

        for neighbour, weight in G[vertex]:
            dist = current_distance + weight

            if dist < distances[neighbour] and not visited[neighbour]:
                if neighbour == L and counter[vertex] != 3: continue

                distances[neighbour] = dist
                counter[neighbour] = counter[vertex] + 1
                PQ.put((dist, neighbour))

        visited[vertex] = True
    return distances



runtests ( turysta )