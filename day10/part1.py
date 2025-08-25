import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]


"""

"""
with open(infile, "r") as f:

  board = [[int(el) for el in line.split(" ")] for line in f.read().strip().splitlines()]

  candidates1 = [sum(line) for line in board]
  candidates2 = [sum(col) for col in zip(*board)]

  print(min(candidates1 + candidates2))
