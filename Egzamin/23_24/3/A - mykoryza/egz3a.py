from gpxpy.geo import distance
from egz3atesty import runtests
from collections import deque

inf = float('inf')

def BFS(G, T, d):
  n = len(G)
  Q = deque()
  result = 1

  type = [None for _ in range(n)]

  for i in range(len(T)):
    type[T[i]] = i
    Q.append(T[i])

  while len(Q) > 0:
    vertex = Q.popleft()

    for neighbour in G[vertex]:
      if type[neighbour] == None:
        type[neighbour] = type[vertex]
        if type[vertex] == d:
          result += 1
        Q.append(neighbour)
  return result


def mykoryza( G,T,d ):
  return BFS(G, T, d)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
