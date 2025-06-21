from queue import PriorityQueue

from numpy.ma.core import floor

from egz1atesty import runtests
inf = float('inf')
def armstrong( B, G, s, t):
  G = adj_list(G)

  dist_s_t = dijkstra(G, s)
  dist_t_s = dijkstra(G, t)

  result = dist_s_t[t]

  for u, p, q in B:
    result = min(result, dist_s_t[u]+dist_t_s[u]*(p/q))

  return floor(result)

def adj_list(G):
  num_of_nodes = max(max(u,v) for u, v, _ in G) + 1

  list = [[] for _ in range(num_of_nodes)]

  for u, v, w in G:
    list[u].append((v, w))
    list[v].append((u, w))

  return list

def dijkstra(G, s):
  n = len(G)

  dist = [inf]*n
  PQ = PriorityQueue()

  dist[s] = 0
  PQ.put((0, s))

  while not PQ.empty():
    d, u = PQ.get()

    if d > dist[u]:
      continue
    for v, w in G[u]:
      alt = dist[u]+w
      if dist[v] > alt:
        dist[v] = alt
        PQ.put((alt, v))
  return dist


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
