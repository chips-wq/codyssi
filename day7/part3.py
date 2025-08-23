import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

# 1 2 3 4 5 6
# x       y
def swap_block(arr : list[int], swap : tuple[int, int]):
  x, y = swap
  # assume y > x
  if y < x: x, y = y, x
  # what is the size of the block
  sz = min(y - x, len(arr) - y)

  print(sz)
  for i in range(sz):
    arr[x+i], arr[y+i] = arr[y+i], arr[x+i]

with open(infile) as f:
  contents = f.read()
  p1, p2, p3 = contents.split("\n\n")

  arr = [int(el) for el in p1.splitlines()]

  classic_swaps = []
  for swap in p2.splitlines():
    i1, i2 = swap.split("-")
    i1 = int(i1) - 1
    i2 = int(i2) - 1
    swap_block(arr, (i1, i2))


  test_index = int(p3.strip()) - 1
  print(arr[test_index])
