# {ADD/SUB/MULTIPLY} {amount} ALL

from commands.abc_command import Instruction
from commands.constants import MOD

class AddAllInstruction(Instruction):
  def __init__(self, amount : int):
    self.amount = amount

  def execute(self, grid: list[list[int]]):
    n, m = len(grid), len(grid[0])
    for i in range(n):
      for j in range(m):
        grid[i][j] += self.amount
        grid[i][j] %= MOD

