import sys
import string

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

def mapping(c : str):
  assert c in string.ascii_letters
  if c in string.ascii_lowercase:
    return ord(c) - ord('a') + 1
  elif c in string.ascii_uppercase:
    return ord(c) - ord('A') + 27



for line in open(infile):
  line = line.strip()

  ans = [ch for ch in line if ch in string.ascii_letters]
  print(len(ans))

  