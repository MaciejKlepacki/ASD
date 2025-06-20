from kol2testy import runtests
from math import inf
from queue import PriorityQueue

def get_adj_list(edges):
    n = max(map(lambda x: max(x[0], x[1]), edges)) + 1
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph, n


def warrior(G, s, t):
    adj, n = get_adj_list(G)

    dist = [[inf] * 17 for _ in range(n)]
    dist[0] = [0] * 17

    queue = PriorityQueue()
    queue.put((0, s, 16))

    while not queue.empty():
        d, u, stamina = queue.get()

        if d > dist[u][stamina]:
            continue

        for v, w in adj[u]:
            real_w = w
            real_stamina = stamina

            if real_w > real_stamina:
                real_w += 8
                real_stamina = 16

            real_stamina -= w

            if dist[v][real_stamina] > d + real_w:
                dist[v][real_stamina] = d + real_w
                queue.put((dist[v][real_stamina], v, real_stamina))

    return min(dist[t])

print(warrior([ (1,5,10), (4,6,12), (3,2,8),
          (2,4,4) , (2,0,10), (1,4,5),
          (1,0,6) , (5,6,8) , (6,3,9)],
          0,
          6))

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( warrior, all_tests = False )

"""
Straight Facts:

In the main loop (*)

1) dist[u][v], dist[u][k] and dist[k][u] are
lengths of paths between nodes, which intermediate
nodes are from set V = { 1, ..., k - 1 }.

2) We can check if dist[u][v] > dist[u][k] + dist[k][v]
and if so, replace the shortest path between u and v
with one that contains k as intermediate node.
"""
from math import inf