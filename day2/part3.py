import sys

infile = "part1.txt" if len(sys.argv) < 2 else sys.argv[1]

def A(num : int):
  return num + 945

def B(num : int):
  return num * 65

def Aex(num : int):
  return num + 495

def Bex(num : int):
  return num * 55

def C(num : int):
  return num ** 3

with open(infile, "r") as f:
  lines = f.read().strip().splitlines()
  lines = [int(num) for num in lines[4:]]
  elems = lines

  ans = 0
  for el in elems:
    if A(B(C(el))) < 15000000000000:
      ans = max(ans, el)

  print(ans)
