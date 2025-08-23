import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

points = []
# Ask about 
for line in open(infile):
  line = line.strip().replace("(", "").replace(")", "")
  
  x, y = line.split(", ")
  x, y = int(x), int(y)

  points.append((x,y))

dists = [abs(x) + abs(y) for x,y in points]

print(min(dists))
print(max(dists))

print(max(dists) - min(dists))


  