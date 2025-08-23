import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

with open(infile) as f:
  contents = f.read()
  p1, p2, p3 = contents.split("\n\n")

  arr = [int(el) for el in p1.splitlines()]

  classic_swaps = []
  for swap in p2.splitlines():
    i1, i2 = swap.split("-")
    i1 = int(i1) - 1
    i2 = int(i2) - 1
    classic_swaps.append((i1, i2))

  classic_swaps.append(classic_swaps[0])
  new_swaps = []
  for i in range(len(classic_swaps) - 1):
    x, y = classic_swaps[i]
    z, _ = classic_swaps[i+1]
    new_swaps.append((x,y,z))

  print(arr)
  for (x, y, z) in new_swaps:
    # arr[x], arr[y], arr[z] = arr[y], arr[z], arr[x]
    arr[y], arr[z], arr[x] = arr[x], arr[y], arr[z]
    print(arr)


  test_index = int(p3.strip()) - 1
  print(arr[test_index])
