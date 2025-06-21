import queue

from markdown_it.rules_block import table

from egz1Atesty import runtests
from queue import PriorityQueue

inf = float('inf')

def dijkstra(G, s, r = None):
  n = len(G)
  dist = [inf for _ in range(n)]
  # if r is None: dist[s] = 0
  # else: dist[s] = -1*rob_v
  dist[s] = 0
  PQ = PriorityQueue()
  PQ.put((0, s))

  while not PQ.empty():
    v_dist, v = PQ.get()

    if v_dist > dist[v]:
      continue

    for u, w in G[v]:
      if r is None:
        if dist[u] > dist[v] + w:
          dist[u] = dist[v] + w
          PQ.put((dist[u], u))
      else:
        if dist[u] > dist[v] + 2*w + r:
          dist[u] = dist[v] + 2*w + r
          PQ.put((dist[u], u))

  return dist


def gold(G,V,s,t,r):

  dist_s = dijkstra(G, s)

  mini = dist_s[t]
  for i in range(len(G)):
    dist_i_t = dijkstra(G, i, r)[t] - V[i]
    mini = min(mini, dist_i_t + dist_s[i])

  return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
