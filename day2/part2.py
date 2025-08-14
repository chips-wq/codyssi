import sys

infile = "part1.txt" if len(sys.argv) < 2 else sys.argv[1]

def A(num : int):
  return num + 945

def B(num : int):
  return num * 65

def C(num : int):
  return num ** 3

with open(infile, "r") as f:
  lines = f.read().strip().splitlines()
  lines = [int(num) for num in lines[4:]]
  lines.sort()

  elems = [el for el in lines if el % 2 == 0]
  print(A(B(C(sum(elems)))))
