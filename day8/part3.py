import sys
import string

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

def is_digit(c : str):
  return c >= '0' and c <= '9'

def can_reduce(a : str, b : str):
  o1 = is_digit(a) and b in (string.ascii_lowercase)
  o2 = is_digit(b) and a in (string.ascii_lowercase)
  return o1 or o2

def reduce(line : str):
  ans = ""
  i = 0
  finished = True
  while i < len(line) - 1:
    if can_reduce(line[i], line[i+1]):
      finished = False
      i += 2
      continue
    ans += line[i]
    i += 1

  if i == len(line) - 1:
    ans += line[i]

  return (finished, ans)

def reduce_all(line : str):
  finished, line = reduce(line)
  while not finished:
    finished, line = reduce(line)
  return line

ans = 0
for line in open(infile):
  line = line.strip()


  line = reduce_all(line)


  ans += len(line)
print(ans)
