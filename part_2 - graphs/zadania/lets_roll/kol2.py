# Maciej Klepacki
# Robię R razy Dijkstrę dla najbliższego resortu, usuwam wszystkie wierzchołki po których przeszedłem i tak R razy.
# Podwojone outputy dodaję do zmiennej total i na koniec zwracam. Pomysł powinien być dobry.

from kol2testy import runtests
from math import inf
from queue import PriorityQueue

def edge_list_to_adj_list(edge_list, num_nodes=None):
    if num_nodes is None:
        num_nodes = max(max(u, v) for u, v, _ in edge_list) + 1
    
    adj_list = [[] for _ in range(num_nodes)]

    for u, v, w in edge_list:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    return adj_list


def dijkstra(G, s):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[s] = 0

    PQ = PriorityQueue()
    PQ.put((0, s))

    while not PQ.empty():
        current_distance, vertex = PQ.get()  

        if current_distance > distance[vertex]: 
            continue 

        for neighbour, weight in G[vertex]:
            dist = current_distance + weight

            if dist < distance[neighbour] and not visited[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                PQ.put((dist, neighbour))

        visited[vertex] = True
    return distance, parent


def remove_vertices(G, vertices_to_remove):
    vertices_to_remove = set(vertices_to_remove)
    for i in range(len(G)):
        if i not in vertices_to_remove:
            G[i] = [(v, w) for v, w in G[i] if v not in vertices_to_remove]

    for v in vertices_to_remove:
        G[v] = []

    return G


def lets_roll(start_city, flights, resorts):
    total = 0
    flights = edge_list_to_adj_list(flights)
    
    for _ in range(len(resorts)):  # Maksymalnie tyle iteracji, ile jest kurortów
        dist, parent = dijkstra(flights, start_city)
        
        # Znajdź najbliższy kurort
        nearest_resort = None
        min_distance = inf
        for resort in resorts:
            if dist[resort] < min_distance:
                min_distance = dist[resort]
                nearest_resort = resort
        
        if nearest_resort is None or min_distance == inf:
            break  # Jeśli nie można dotrzeć do żadnego kurortu, zakończ

        total += min_distance

        # Odtwórz ścieżkę do najbliższego kurortu
        path = []
        current = nearest_resort
        while current is not None:
            path.append(current)
            current = parent[current]
        
        # Usuń wierzchołki ze ścieżki
        remove_vertices(flights, path)

    return 2 * total  # Wynik to podwojona suma odległości


# Testowanie funkcji
runtests(lets_roll, all_tests=False)