import sys

infile = "part1.txt" if len(sys.argv) < 2 else sys.argv[1]

"""

c    d
------
   -------
   a     b

a    b
------
   -------
   c     d

a------------b
    c---------------d


a-----------------------b
     c----------d
"""

"""
Inclusion-Exclusion principle

a----b
              <- number of unique things
  b-----c

d---e

 g----------e

len(A1) + len(A2) + len(A3) + len(A4) <- C_4^1 = 4
- len(A1 and A2) - len(A1 and A3) - len(A1 and A4) - len(A2 and A3) - len(A2 and A4) - len(A3 and A4) <- C_4^2 = 6
+ len(A1 and A2 and A3) + len(A1 and A3 and A4) + len(A1 and A2 and A4) + len(A2 and A3 and A4) <- C_4^3 = 
- len(A1 and A2 and A3 and A4) C_4^4 = 1

"""

def intersect(interval1 : tuple[int, int], interval2 : tuple[int, int]) -> tuple[int, int]:
  if interval1 == (1,0) or interval2 == (1,0): return (1,0)
  a, b = interval1
  c, d = interval2
  # I would like interval1 to start first
  if a > c:
    a,c = c,a
    d,b = b,d

  # You now need their intersection
  if (b >= c):
    right = min(b,d)
    return (c, right)
  return (1, 0)

def sz(interval : tuple[int, int]) -> int:
  return interval[1] - interval[0] + 1

def parse_intervals(line : str) -> list[tuple[int, int]]:
    r1, r2 = line.split(" ")
    a, b = [int(el) for el in r1.split("-")]
    c, d = [int(el) for el in r2.split("-")]
    return [(a,b), (c,d)]

with open(infile, "r") as f:
  content = f.read()
  ans = 0

  lines = content.splitlines()

  for i in range(0, len(lines)-1):
    line1, line2 = lines[i:i+2]
    i1, i2 = parse_intervals(line1)
    i3, i4 = parse_intervals(line2)

    """
        len(A1) + len(A2) + len(A3) + len(A4) <- C_4^1 = 4
    - len(A1 and A2) - len(A1 and A3) - len(A1 and A4) - len(A2 and A3) - len(A2 and A4) - len(A3 and A4) <- C_4^2 = 6
    + len(A1 and A2 and A3) + len(A1 and A3 and A4) + len(A1 and A2 and A4) + len(A2 and A3 and A4) <- C_4^3 = 
    - len(A1 and A2 and A3 and A4) C_4^4 = 1
    """

    current = 0
    current += sz(i1) + sz(i2) + sz(i3) + sz(i4)
    current -= sz(intersect(i1, i2)) + sz(intersect(i1, i3)) + sz(intersect(i1, i4)) + sz(intersect(i2,i3)) + sz(intersect(i2, i4)) + sz(intersect(i3, i4))

    a1a2a3 = intersect(intersect(i1,i2),i3)
    a1a3a4 = intersect(intersect(i1,i3),i4)
    a1a2a4 = intersect(intersect(i1,i2),i4)
    a2a3a4 = intersect(intersect(i2,i3),i4)

    current += sz(a1a2a3) + sz(a1a3a4) + sz(a1a2a4) + sz(a2a3a4)

    a1a2a3a4 = intersect(intersect(i1,i2), intersect(i3,i4))

    current -= sz(a1a2a3a4)

    ans = max(ans, current)

  print(ans)
