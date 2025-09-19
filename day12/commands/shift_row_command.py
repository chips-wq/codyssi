# SHIFT {ROW/COL} {number} BY {shift amount}

from commands.abc_command import Instruction

class ShiftRowInstruction(Instruction):
  def __init__(self, amount : int, row : int):
    self.amount = amount
    self.row = row

  def execute(self, grid: list[list[int]]):
    row = grid[self.row]
    # Make a copy out of the row and then shift it
    r2 = row.copy()
    
    m = len(row)
    i = m-self.amount
    for j in range(m):
      r2[j] = row[i%m]
      i += 1
    
    grid[self.row] = r2


