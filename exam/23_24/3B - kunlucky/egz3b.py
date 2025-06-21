from egz3btesty import runtests
from queue import deque

def kunlucky_set(T, k, n):
  kset = set()
  x = k
  kset.add(k)
  for i in range(1, n):
    x = x+(x%i)+7
    kset.add(x)
  return kset

def lucky_arr(T, kset, n):
  for i in range(n):
      T[i] = T[i] in kset
  return T


def kunlucky(T, k):
  n = len(T)

  kset = kunlucky_set(T, k, n)

  T = lucky_arr(T, kset, n)

  maxi = 0
  kt = deque()
  kt.append(0)

  for i in range(n):
    if T[i]:
      if len(kt)==1: kt.append(i)
      elif len(kt)==2: kt.append(i)
      else:
        l = kt.popleft()
        r = i-1
        kt.append(i)
        maxi = max(maxi, r-l)
  maxi = max(maxi, n-1-kt[0])

  return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )
