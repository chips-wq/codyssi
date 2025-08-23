# Let's try splitting this up first in a line and then in a generator
import sys

infile = "exampl1.in" if len(sys.argv) < 2 else sys.argv[1]

def custom_split(line : str):
  ans, c = [], line[0]

  for ch in line[1:]:
    if ch == c[-1]:
      c += ch
    else:
      ans.append(c)
      c = ch
  ans.append(c)
  return ans

def reunite_splits(ans : list[str]):
  return "".join(str(len(sp)) + sp[0] for sp in ans)


def mem(c : str):
  if c >= 'A' and c <= 'Z':
    return ord(c) - ord('A') + 1
  assert c >= '0' and c <= '9'
  return ord(c) - ord('0')


def line_mem(line : str) -> int:
  return sum(mem(ch) for ch in line)

ans = 0
for line in open(infile):
  line = line.strip()

  res = custom_split(line)
  res = reunite_splits(res)
  print(f"{res} - {line_mem(res)}")

  ans += line_mem(res)

print(ans)
