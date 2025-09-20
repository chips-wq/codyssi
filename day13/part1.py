from collections import deque, defaultdict
import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

"""
graph[some_str] -> [l1, l2, l3]
"""

with open(infile, "r") as f:
  graph = defaultdict(list)

  lines = f.read().strip().splitlines()
  for line in lines:
    edge_str, path_len = line.split("|")
    path_len = int(path_len.strip())

    fro, to = edge_str.strip().split("->")
    fro = fro.strip()
    to = to.strip()

    graph[fro].append(to)

    print(f"{fro} -> {to}")

  
  start = "STT"
  q = deque([start])

  dist = defaultdict(int)
  visited = set(start)
  
  while q:
    c_node = q.popleft()

    for neigh in graph[c_node]:
      if neigh in visited: continue
      dist[neigh] = dist[c_node] + 1
      visited.add(neigh)
      q.append(neigh)

  path_lengths = [ll for ll in dist.values()]
  path_lengths.sort(reverse=True)
  print(path_lengths)
  r = path_lengths[:3]
  print(r[0] * r[1] * r[2])



  

    

