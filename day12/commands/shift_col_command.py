# SHIFT {ROW/COL} {number} BY {shift amount}

from commands.abc_command import Instruction

class ShiftColumnInstruction(Instruction):
  def __init__(self, amount : int, column : int):
    self.amount = amount
    self.column = column

  def execute(self, grid: list[list[int]]):
    n, _ = len(grid), len(grid[0])

    column = [0] * n
    col2 = [0] * n
    for i in range(n):
      column[i] = grid[i][self.column]

    j = n - self.amount
    for i in range(n):
      col2[i] = column[j%n]
      j += 1
    
    # Then copy back col2 inside of grid[i][self.column]
    for i in range(n):
      grid[i][self.column] = col2[i]
