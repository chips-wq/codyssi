import sys

infile = "exampl1.in" if len(sys.argv) < 2 else sys.argv[1]

ans = 0
for line in open(infile):
  line = line.strip()
  memory = [ord(ch) - ord('A') + 1 for ch in line]
  print(sum(memory))
  ans += sum(memory)

print(ans)
