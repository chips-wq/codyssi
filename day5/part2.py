import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

points = []
# Ask about 
for line in open(infile):
  line = line.strip().replace("(", "").replace(")", "")
  
  x, y = line.split(", ")
  x, y = int(x), int(y)

  points.append((x,y))

def closest_to(point, points : list[tuple[int, int]]) -> int:
  x1,y1 = point

  ans = 0
  for i, (x2, y2) in enumerate(points):
    # d is current distance between this point and our current point
    d = abs(x2-x1) + abs(y2-y1)
    if d == 0: continue
    # d2 is smallest distance we have seen so far
    x3, y3 = points[ans]
    d2 = abs(x3 - x1) + abs(y3-y1)
    if d < d2:
      ans = i

  return ans
  
points.sort()

i1 = closest_to((0, 0), points)
i2 = closest_to(points[i1], points)
print(points[i1])
print(points[i2])

x1, y1 = points[i1]
x2, y2 = points[i2]

print(abs(x2-x1) + abs(y2-y1))


  