from collections import deque, defaultdict
import heapq
import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

"""
graph[some_str] -> [l1, l2, l3]
"""

INF = 10 ** 18 + 5

with open(infile, "r") as f:
  graph = defaultdict(list)

  lines = f.read().strip().splitlines()
  for line in lines:
    edge_str, cost = line.split("|")
    cost = int(cost.strip())

    fro, to = edge_str.strip().split("->")
    fro = fro.strip()
    to = to.strip()

    graph[fro].append((to, cost))

    print(f"{fro} -> {to}")

  
  start = "STT"
  q = [(0, start)]

  dist = defaultdict(lambda: INF)
  dist[start] = 0
  visited = set()
  
  while q:
    c_dist, c_node = heapq.heappop(q)

    if c_node in visited: continue
    visited.add(c_node)


    for (neigh, cost) in graph[c_node]:
      if dist[c_node] + cost < dist[neigh]:
        dist[neigh] = dist[c_node] + cost
        heapq.heappush(q, (dist[neigh], neigh))

  print(dist)
  path_lengths = [ll for ll in dist.values()]
  path_lengths.sort(reverse=True)
  print(path_lengths)
  r = path_lengths[:3]
  print(r[0] * r[1] * r[2])



  

    

