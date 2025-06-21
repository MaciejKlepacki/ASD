from math import inf
from queue import PriorityQueue


def dijkstra(G, s):
    n = len(G)
    parents = [None] * n

    dist = [inf] * n
    dist[s] = 0

    queue = PriorityQueue()
    queue.put((dist[s], s))

    while not queue.empty():
        v_dist, v = queue.get()

        # If we have already found a shorter path
        # to v, continue.
        if v_dist > dist[v]:
            continue

        for u, w in G[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                parents[u] = v
                queue.put((dist[u], u))

    return dist, parents