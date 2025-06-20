from zad3testy import runtests
from queue import PriorityQueue

def longer( G, s, t ):
    def dijkstra(G, s):
        n = len(G)
        distance = [float("inf") for _ in range(n)]
        parent = [None for _ in range(n)]
        visited = [False for _ in range(n)]
        distance[s] = 0

        Q = PriorityQueue()
        Q.put((0, s))

        while not Q.empty():

            (cur_distance, v) = Q.get()

            if cur_distance > distance[v]: continue

            for v_son, weight in G[v]:
                dist = cur_distance + weight

                if dist < distance[v_son] and not visited[v_son]:
                    distance[v_son] = dist
                    parent[v_son] = v
                    Q.put((dist, v_son))
            visited[v] = True
        return distance
    return (0,0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = False )
