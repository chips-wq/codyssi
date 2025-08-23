import sys
from typing import Optional

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

"""
These form a graph, each point, could visit any other point, but:
G(V, E)

for any (x, y) there is an edge (x,y) with the cost as the manhattan distance

Use dijkstra (in order to always take the lowest cost)

Option2:

Always compute the closest point, that is not in visited



()
|
|
()--------               ()  
         |
         ()

  ()                     ()




"""
points = []
# Ask about 
for line in open(infile):
  line = line.strip().replace("(", "").replace(")", "")
  
  x, y = line.split(", ")
  x, y = int(x), int(y)

  points.append((x,y))

def closest_to(point, points : list[tuple[int, int]], seen : list[tuple[int, int]]) -> Optional[int]:
  x1,y1 = point

  # Take the closest point to (x1, y1) out of points which is not in seen
  # Do a distance with index

  ans = [(abs(x2 - x1) + abs(y2 - y1), i) for i, (x2,y2) in enumerate(points) if (x2,y2) not in seen]
  ans.sort()
  if len(ans) == 0:
    return None
  return ans[0][1]


def shortest_path(start : tuple[int, int]):
  x, y = start

  path = [(x,y)]

  # Choose closest one, add it to visited
  while (index_new := closest_to(path[-1], points, path)) != None:
    path.append(points[index_new])
    print(points[index_new])

  ans = 0
  for i in range(1, len(path)):
    x1, y1 = path[i-1]
    x2, y2 = path[i]
    ans += abs(x2 - x1) + abs(y2-y1)

  print(ans)
  return ans

points.sort()

shortest_path((0, 0))

  