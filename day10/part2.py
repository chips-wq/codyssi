import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]


TARGET_ROW_COL = 15
"""
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + board[i][j]
"""

INF = 10 ** 18

with open(infile, "r") as f:
  board = [[int(el) for el in line.split(" ")] for line in f.read().strip().splitlines()]
  n = len(board)
  assert n == len(board[0])
  # Let's pad this with zeros
  for i in range(n):
    board[i].insert(0, 0)
  board.insert(0, [0] * (n + 1))

  dp = [[INF] * (n+1) for _ in range(n+1)]
  dp[0][1] = dp[1][0] = 0

  for i in range(1, n+1):
    for j in range(1, n+1):
      dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + board[i][j]

  print(dp[n][n])
