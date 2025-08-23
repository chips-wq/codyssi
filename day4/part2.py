import sys

infile = "exampl1.in" if len(sys.argv) < 2 else sys.argv[1]

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

  kept = len(line) // 10
  res = line[:kept] + str(len(line) - 2 * kept) + line[::-1][:kept]

  print(f"{res} - {line_mem(res)}")
  ans += line_mem(res)

print(ans)
