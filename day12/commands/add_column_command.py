# {ADD/SUB/MULTIPLY} {amount} {ROW/COL} {number}

from commands.constants import MOD
from commands.abc_command import Instruction

class AddColumnInstruction(Instruction):
  def __init__(self, amount : int, column : int):
    self.amount = amount
    self.column = column

  def execute(self, grid: list[list[int]]):
    n, _ = len(grid), len(grid[0])
    
    for i in range(n):
      grid[i][self.column] += self.amount
      grid[i][self.column] %= MOD
