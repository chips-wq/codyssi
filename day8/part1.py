import sys
import string

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

ans = 0
for line in open(infile):
  line = line.strip()

  alph = [ch for ch in line if ch in string.ascii_lowercase]
  ans += len(alph)
print(ans)
