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

with open(infile, "r") as f:
  content = f.read()
  ans = 0
  for line in content.splitlines():
    r1, r2 = line.split(" ")
    a, b = [int(el) for el in r1.split("-")]
    c, d = [int(el) for el in r2.split("-")]

    if a > c:
      a,c = c,a
      d,b = b,d

    current = 0
    current += sz((a,b)) + sz((c,d))
    # You now need their intersection
    current -= sz(intersect((a,b), (c,d)))

    print(current)
    ans += current

  print(ans)
