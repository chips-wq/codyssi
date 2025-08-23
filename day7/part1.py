import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

with open(infile) as f:
  contents = f.read()
  p1, p2, p3 = contents.split("\n\n")

  arr = [int(el) for el in p1.splitlines()]

  for swap in p2.splitlines():
    i1, i2 = swap.split("-")
    i1 = int(i1) - 1
    i2 = int(i2) - 1
    arr[i1], arr[i2] = arr[i2], arr[i1]

  test_index = int(p3.strip()) - 1
  print(arr[test_index])
